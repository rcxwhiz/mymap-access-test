from classroom import semester_manager
from gui.startup import StartupWindow

test_semester = 'Fall 201944'

semester_bag = semester_manager.SemesterManager()
if test_semester not in semester_bag.cached_semesters():
	semester_bag.update(test_semester)

print(semester_bag.semester(test_semester).datestamp)

StartupWindow()
