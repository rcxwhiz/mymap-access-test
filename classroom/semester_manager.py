from __future__ import annotations

import re
import pickle
import os
import sys
from pathlib import Path
from typing import Optional
from classroom import semester_getter
import classroom


class SemesterManagerMeta(type):
	_instance: Optional[SemesterManager] = None

	def __call__(self) -> SemesterManager:
		if self._instance is None:
			self._instance = super().__call__()
		return self._instance


class SemesterManager(metaclass=SemesterManagerMeta):

	def __init__(self):
		self.semesters = {}

		self.pickles_path = os.path.join(os.path.dirname(Path(sys.argv[0]).parent), 'pickles')
		if not os.path.exists(self.pickles_path):
			os.makedirs(self.pickles_path)

		for file in os.listdir(self.pickles_path):
			self.semesters[file] = pickle.load(open(os.path.join(self.pickles_path, file), 'rb'))

		self.selected_semester = None
		self.filtered_sections = []

		self.dept_filter = ''
		self.course_num_filter = ''
		self.course_name_filter = ''
		self.instructor_filter = ''
		self.time_filter = [0, 0]
		self.type_filter = {'DAY': False,
		                    'EVENING': False,
		                    'ONLINE': False,
		                    'SALT LAKE': False,
		                    'ST ABROAD': False}
		self.day_filter = {'M': [0, 0, False],
		                   'T': [0, 0, False],
		                   'W': [0, 0, False],
		                   'Th': [0, 0, False],
		                   'F': [0, 0, False],
		                   'Sa': [0, 0, False]}
		self.credits_filter = [0.0, 0.0]  # MIN - MAX
		self.course_level_filter = {100: False,
		                            200: False,
		                            300: False,
		                            400: False,
		                            500: False,
		                            600: False,
		                            700: False}

	def semester(self, semester_year):
		if semester_year in self.semesters.keys():
			return self.semesters[semester_year]
		print(f'Requested semester {semester_year} not in semester manager')
		return None

	def update(self, semester_year):
		self.semesters[semester_year] = semester_getter.get(semester_year)
		if os.path.exists(os.path.join(self.pickles_path, semester_year)):
			os.remove(os.path.join(self.pickles_path, semester_year))
		if self.semesters[semester_year] is not None:
			pickle.dump(self.semesters[semester_year], open(os.path.join(self.pickles_path, semester_year), 'wb'))

	def cached_semesters(self):
		return list(self.semesters.keys())

	def select_semester(self, semester_year):
		self.selected_semester = self.semesters[semester_year]

	def num_sections(self):
		return len(self.filtered_sections)

	def find_same_course(self, list_in, course):
		for i in range(len(list_in)):
			if course.short_title == list_in[i].short_title:
				if 'R' in course.short_title:
					print(f'Found an R course in {course.short_title}')
				return i

	def del_section(self, sections, section_num):
		for section in sections:
			if section.section_num == section_num:
				sections.remove(section)
				return None
		print('Did not find a section')

	def get_sections_by_course(self, courses, short_name):
		for course in courses:
			if course.short_title == short_name:
				return course.sections
		print('Did not find a course')

	def class_in_slot(self, day, section):
		for slot in section.schedule:
			if slot[0] != day:
				continue
			if slot[1] >= self.day_filter[day][0] and slot[2] <= self.day_filter[day][1]:
				return True
		return False

	def get_filtered_semester(self):
		semester_attributes = {'timestamp': self.selected_semester.timestamp,
		              'datestamp': self.selected_semester.datestamp,
		              'courses': [],
		              'semester year': self.selected_semester.semester_year}

		for course in self.selected_semester.courses:
			course_attributes = {'dept': course.dept,
			                     'num': course.num,
			                     'long title': course.long_title,
			                     'description': course.description,
			                     'college short': course.college_short,
			                     'college long': course.college_long,
			                     'courseCredits': course.hours,
			                     'courseOffered': course.offered,
			                     'courseHeaders': course.headers,
			                     'courseNote': course.note,
			                     'courseWhenTaught': course.when_taught,
			                     'coursePrereqs': course.prerequisites,
			                     'courseRec': course.recommended,
			                     'sections': []}
			if self.dept_filter not in course.dept:
				continue

			elif self.course_num_filter not in str(course.num):
				continue

			elif self.course_name_filter not in course.long_title:
				continue

			elif True in self.course_level_filter.values() and not self.course_level_filter[course.level]:
				continue

			for section in course.sections:
				make_section = True
				if self.instructor_filter not in section.instructor:
					make_section = False

				elif True in self.type_filter.values() and not self.type_filter[section.type]:
					make_section = False

				elif self.credits_filter[0] != 0 or self.credits_filter[1] != 0:
					if not (self.credits_filter[0] <= section.credits <= self.credits_filter[1]):
						make_section = False

				for day in self.day_filter.keys():
					if self.day_filter[day][2]:
						if not self.class_in_slot(day, section):
							make_section = False

				if make_section:
					section_attributes = {'section num': section.section_num,
					                      'type': section.type,
					                      'instructor': section.instructor,
					                      'credits': str(section.credits),
					                      'term': section.term,
					                      'days': section.days,
					                      'starts': section.start,
					                      'ends': section.end,
					                      'loction': section.loction,
					                      'available': section.available_frac,
					                      'waitlist': section.waitlist}
					course_attributes['sections'].append(classroom.section.Section(section_attributes))

			if len(course.sections) > 0:
				semester_attributes['courses'].append(classroom.course.Course(course_attributes))

		return classroom.semester.Semester(semester_attributes)

	def remove_semester(self, semester_year):
		del self.semesters[semester_year]
		if os.path.exists(semester_year):
			os.remove(semester_year)
