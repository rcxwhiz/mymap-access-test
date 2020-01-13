from classroom import semester_manager
from gui import startup_page

test_semester = 'Fall 2019'

semester_bag = semester_manager.SemesterManager()
if test_semester not in semester_bag.cached_semesters():
	semester_bag.update(test_semester)

print(semester_bag.semester(test_semester).datestamp)

startup_page.main()
