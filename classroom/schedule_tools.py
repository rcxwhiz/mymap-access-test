from classroom.semester_manager import SemesterManager

semester_manager = SemesterManager()


def get_combinations():
	if semester_manager.selected_semester is None:
		return None


def filter_combinations():
	if semester_manager.selected_semester is None:
		return None
