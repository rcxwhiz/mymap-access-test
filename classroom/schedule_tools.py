import itertools

from classroom.semester_manager import SemesterManager

semester_manager = SemesterManager()


def schedule_collision(class1, class2):
	for meeting in class1.schedule:
		for other_meeting in class2.schedule:
			if meeting[0] == other_meeting[0]:
				if meeting[1] < other_meeting[1] and meeting[2] < other_meeting[2]:
					return False
				elif meeting[1] > other_meeting[1] and meeting[2] > other_meeting[2]:
					return False
				else:
					return True
	return False


def get_combinations(class_list):
	if semester_manager.selected_semester is None:
		return None

	possible_sections = []
	for i, course in enumerate(class_list):
		for semester_course in semester_manager.selected_semester.courses:
			if course == semester_course.short_title:
				if len(possible_sections) == i:
					possible_sections.append(semester_course.sections)
				else:
					for listing_sections in semester_course.sections:
						possible_sections[i].append(listing_sections)

	return filter_combinations(possible_sections)


def filter_combinations(possible_sections):
	unfiltered_schedules = itertools.product(*possible_sections)
	good_schedules = []
	for possible_schedule in unfiltered_schedules:
		add_this_schedule = True
		for combo in itertools.combinations(possible_schedule, 2):
			if schedule_collision(combo[0], combo[1]):
				add_this_schedule = False
				break
		if add_this_schedule:
			good_schedules.append(possible_schedule)
	return good_schedules
