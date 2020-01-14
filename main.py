from classroom import semester_manager
from gui import full_ui

test_semester = 'Fall 2019'

semester_bag = semester_manager.SemesterManager()
if test_semester not in semester_bag.cached_semesters():
	semester_bag.update(test_semester)

print(semester_bag.semester(test_semester).datestamp)

types = []
for course in semester_bag.semester(test_semester).courses:
	for section in course.sections:
		if section.type not in types:
			types.append(section.type)

print(types)

full_ui.main()
