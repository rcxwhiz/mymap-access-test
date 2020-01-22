import itertools

from classroom.semester_manager import SemesterManager

semester_manager = SemesterManager()


def schedule_collision(class1, class2):
	for meeting in class1.schedule:
		for other_meeting in class2.schedule:
			if meeting[0] == other_meeting[0]:
				if meeting[1] < other_meeting[1] and meeting[2] < other_meeting[2]:
					x = 0
				elif meeting[1] > other_meeting[1] and meeting[2] > other_meeting[2]:
					x = 0
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


def earliest_start(schedules_in):
	schedules_in_starts = []

	for schedule in schedules_in:
		schedules_in_starts.append({'M': [1140, 0, 0],
		                            'T': [1140, 0, 0],
		                            'W': [1140, 0, 0],
		                            'Th': [1140, 0, 0],
		                            'F': [1140, 0, 0],
		                            'Sa': [1140, 0, 0]})
		for section in schedule:
			for meeting in section.schedule:
				if schedules_in_starts[-1][meeting[0]][0] > meeting[1]:
					schedules_in_starts[-1][meeting[0]][0] = meeting[1]
				schedules_in_starts[-1][meeting[0]][1] += meeting[1]
				schedules_in_starts[-1][meeting[0]][2] += 1

	minimum_start = 1440
	for sched_stats in schedules_in_starts:
		max_all_week = 1440
		for day in sched_stats.keys():
			max_all_week = max(sched_stats[day][0], max_all_week)
		minimum_start = min(minimum_start, max_all_week)

	working_schedules = []
	working_stats = []
	for i, sched_stats in enumerate(schedules_in_starts):
		max_all_week = 1440
		for day in sched_stats.keys():
			max_all_week = max(sched_stats[day][0], max_all_week)
		if max_all_week == minimum_start:
			working_schedules.append(schedules_in[i])
			working_stats.append(sched_stats)

	minimum_avg = 1440
	for i, sched_stats in enumerate(working_stats):
		weekly_avg = []
		for day in sched_stats.keys():
			if sched_stats[day][1] != 0:
				weekly_avg.append(sched_stats[day][0])
		weekly_avg = sum(weekly_avg) / len(weekly_avg)
		minimum_avg = min(minimum_avg, weekly_avg)

	opt_schedules = []
	for i, sched_stats in enumerate(working_stats):
		weekly_avg = []
		for day in sched_stats.keys():
			if sched_stats[day][1] != 0:
				weekly_avg.append(sched_stats[day][0])
		weekly_avg = sum(weekly_avg) / len(weekly_avg)
		if weekly_avg == minimum_avg:
			opt_schedules.append(working_schedules[i])

	return opt_schedules


def latest_start(schedules_in):
	schedules_in_starts = []

	for schedule in schedules_in:
		schedules_in_starts.append({'M': [1140, 0, 0],
		                            'T': [1140, 0, 0],
		                            'W': [1140, 0, 0],
		                            'Th': [1140, 0, 0],
		                            'F': [1140, 0, 0],
		                            'Sa': [1140, 0, 0]})
		for section in schedule:
			for meeting in section.schedule:
				if schedules_in_starts[-1][meeting[0]][0] > meeting[1]:
					schedules_in_starts[-1][meeting[0]][0] = meeting[1]
				schedules_in_starts[-1][meeting[0]][1] += meeting[1]
				schedules_in_starts[-1][meeting[0]][2] += 1

	maximum_start = 0
	for sched_stats in schedules_in_starts:
		min_all_week = 0
		for day in sched_stats.keys():
			min_all_week = min(sched_stats[day][0], min_all_week)
		maximum_start = max(maximum_start, min_all_week)

	working_schedules = []
	working_stats = []
	for i, sched_stats in enumerate(schedules_in_starts):
		min_all_week = 0
		for day in sched_stats.keys():
			min_all_week = min(sched_stats[day][0], min_all_week)
		if min_all_week == maximum_start:
			working_schedules.append(schedules_in[i])
			working_stats.append(sched_stats)

	maximum_avg = 0
	for i, sched_stats in enumerate(working_stats):
		weekly_avg = []
		for day in sched_stats.keys():
			if sched_stats[day][1] != 0:
				weekly_avg.append(sched_stats[day][0])
		weekly_avg = sum(weekly_avg) / len(weekly_avg)
		maximum_avg = max(maximum_avg, weekly_avg)

	opt_schedules = []
	for i, sched_stats in enumerate(working_stats):
		weekly_avg = []
		for day in sched_stats.keys():
			if sched_stats[day][1] != 0:
				weekly_avg.append(sched_stats[day][0])
		weekly_avg = sum(weekly_avg) / len(weekly_avg)
		if weekly_avg == maximum_avg:
			opt_schedules.append(working_schedules[i])

	return opt_schedules


def earliest(schedules_in):
	start_tallys = []
	for i, schedule in enumerate(schedules_in):
		start_tallys.append(0)
		days = []
		for section in schedule:
			for meeting in section.schedule:
				if meeting[0] not in days:
					days.append(meeting[0])
				start_tallys[i] += meeting[1]
				start_tallys[i] += meeting[2]
		start_tallys[i] /= len(days)

	opt_schedules = []
	for i, schedule in enumerate(schedules_in):
		if start_tallys[i] == min(start_tallys):
			opt_schedules.append(schedule)

	return opt_schedules


def latest(schedules_in):
	start_tallys = []
	for i, schedule in enumerate(schedules_in):
		start_tallys.append(0)
		days = []
		for section in schedule:
			for meeting in section.schedule:
				if meeting[0] not in days:
					days.append(meeting[0])
				start_tallys[i] += meeting[1]
				start_tallys[i] += meeting[2]
		start_tallys[i] /= len(days)

	opt_schedules = []
	for i, schedule in enumerate(schedules_in):
		if start_tallys[i] == max(start_tallys):
			opt_schedules.append(schedule)

	return opt_schedules


def shortest_day(schedules_in):
	day_stats = []
	day_lengths = []
	for i, schedule in enumerate(schedules_in):
		day_stats.append({'M': [1440, 0, 0],
		                  'T': [1440, 0, 0],
		                  'W': [1440, 0, 0],
		                  'Th': [1440, 0, 0],
		                  'F': [1440, 0, 0],
		                  'Sa': [1440, 0, 0]})
		for section in schedule:
			for meeting in section.schedule:
				day_stats[i][meeting[0]][0] = min(day_stats[i][meeting[0]][0], meeting[1])
				day_stats[i][meeting[0]][1] = max(day_stats[i][meeting[0]][1], meeting[2])
				day_stats[i][meeting[0]][2] = day_stats[i][meeting[0]][1] - day_stats[i][meeting[0]][0]
		lengths = []
		for day in day_stats[i].keys():
			lengths.append(day_stats[i][day][2])
		lengths.sort()
		day_lengths.append(lengths)

	to_beat = [1440, 1440, 1440, 1440, 1440, 1440]
	for i in range(len(day_lengths)):
		for j in range(len(day_lengths[i])):
			if day_lengths[i][j] < to_beat[j]:
				to_beat[j] = day_lengths[i][j]
			else:
				break

	opt_schedules = []
	for i, schedule in enumerate(schedules_in):
		if day_lengths[i] == to_beat:
			opt_schedules.append(schedule)

	return opt_schedules
