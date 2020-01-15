from __future__ import annotations

import copy
import pickle
import os
import sys
from typing import Optional
from classroom import semester_getter
from my_logger import logging


class SemesterManagerMeta(type):
	_instance: Optional[SemesterManager] = None

	def __call__(self) -> SemesterManager:
		if self._instance is None:
			self._instance = super().__call__()
		return self._instance


class SemesterManager(metaclass=SemesterManagerMeta):

	def __init__(self):
		self.semesters = {}

		pickles_path = os.path.join(os.path.dirname(sys.argv[0]), 'pickles')
		if not os.path.exists(pickles_path):
			os.makedirs(pickles_path)

		for file in os.listdir(pickles_path):
			self.semesters[file] = pickle.load(open(os.path.join(pickles_path, file), 'rb'))

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
		self.day_filter = {'M': False,
		                   'T': False,
		                   'W': False,
		                   'Th': False,
		                   'F': False,
		                   'Sa': False}
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
		if os.path.exists(semester_year):
			os.remove(semester_year)
		if self.semesters[semester_year] is not None:
			pickle.dump(self.semesters[semester_year], open(semester_year, 'wb'))

	def cached_semesters(self):
		return list(self.semesters.keys())

	def select_semester(self, semester_year):
		self.selected_semester = self.semesters[semester_year]

	def num_sections(self):
		return len(self.filtered_sections)

	def find_same_course(self, list, course):
		for i in range(len(list)):
			if course.short_title == list[i].short_title:
				return i

	def find_same_section(self, list, section):
		for i in range(len(list)):
			if section.section_num == list[i].section_num:
				return i

	def get_filtered_semester(self):

		temp_semester = copy.deepcopy(self.selected_semester)

		temp_courses = copy.deepcopy(temp_semester.courses)
		for course in temp_semester.courses:
			if self.dept_filter not in course.dept:
				del temp_courses[self.find_same_course(temp_courses, course)]

			elif self.course_num_filter not in str(course.num):
				del temp_courses[self.find_same_course(temp_courses, course)]

			elif self.course_name_filter not in course.long_title:
				del temp_courses[self.find_same_course(temp_courses, course)]

			elif True in self.course_level_filter.values():
				if not self.course_level_filter[course.level]:
					del temp_courses[self.find_same_course(temp_courses, course)]

			if self.find_same_course(temp_courses, course) is not None:
				temp_sections = copy.deepcopy(temp_courses[self.find_same_course(temp_courses, course)].sections)

				for section in course.sections:
					if self.instructor_filter not in section.instructor:
						del temp_sections[self.find_same_section(temp_sections, section)]

					elif True in self.type_filter.values():
						if not self.type_filter[section.type]:
							del temp_sections[self.find_same_section(temp_sections, section)]

					elif True in self.day_filter.values():
						for day in self.day_filter.keys():
							if self.day_filter[day] and day not in section.days:
								del temp_sections[self.find_same_section(temp_sections, section)]

					elif self.credits_filter[0] != 0 and self.credits_filter[1] != 0:
						if not section.credits > self.credits_filter[0] or not section.credits < self.credits_filter[1]:
							del temp_sections[self.find_same_section(temp_sections, section)]

				temp_courses[self.find_same_course(temp_courses, course)].sections = temp_sections
		temp_semester.courses = temp_courses
		# ALL TESTS HAVE BEEN PASSED
		return temp_semester

	def remove_semester(self, semester_year):
		del self.semesters[semester_year]
		if os.path.exists(semester_year):
			os.remove(semester_year)
