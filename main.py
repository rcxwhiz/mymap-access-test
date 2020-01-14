from classroom import semester_manager
from gui import full_ui

test_semester = 'Fall 2019'

semester_bag = semester_manager.SemesterManager()

semester_bag.select_semester(test_semester)

full_ui.main()
