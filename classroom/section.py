import datetime
import logging
import re

class Section:

	def __init__(self, attributes):
		logging.debug('Creating a new section')
		self.section_num = int(attributes['section num'])
		self.type = attributes['type']
		self.instructor = attributes['instructor']
		self.credits = float(re.findall(r'\d+\.\d+', attributes['credits'])[0])
		self.term = attributes['term']
		self.days = attributes['days']
		self.start = attributes['starts']
		self.end = attributes['ends']
		self.loction = attributes['loction']
		self.available_frac = attributes['available']
		self.waitlist = int(attributes['waitlist'])

		self.schedule = []
		for i, meeting in enumerate(self.days.split('\n')):
			start_time_string = self.start.split('\n')[i]
			end_time_string = self.end.split('\n')[i]
			if ':' in start_time_string:
				start_time = datetime.datetime.strptime(start_time_string, '%I:%M %p')
			else:
				start_time = datetime.datetime.strptime(start_time_string, '%I %p')
			if ':' in end_time_string:
				end_time = datetime.datetime.strptime(end_time_string, '%I:%M %p')
			else:
				end_time = datetime.datetime.strptime(end_time_string, '%I %p')

			start_time = start_time.hour * 60 + start_time.minute
			end_time = end_time.hour * 60 + end_time.minute
			for j, day in enumerate(meeting):
				if day == 'h' or day == 'a':
					continue
				elif day == 'T':
					if meeting[j + 1] == 'h':
						print('thu')
						self.schedule.append(['Th', start_time, end_time])
					else:
						print('tue')
						self.schedule.append(['T', start_time, end_time])
				elif day == 'M':
					print('mon')
					self.schedule.append(['M', start_time, end_time])
				elif day == 'W':
					print('wed')
					self.schedule.append(['W', start_time, end_time])
				elif day == 'F':
					print('fri')
					self.schedule.append(['F', start_time, end_time])
				elif day == 'S':
					print('sat')
					self.schedule.append(['Sa', start_time, end_time])

		building_regex = re.compile(r'[a-zA-Z]*')
		self.building = building_regex.search(attributes['loction']).group()

		available_regex1 = re.compile(r'[0-9]+/')
		available_regex2 = re.compile(r'/[0-9]+')
		self.available = int(available_regex1.search(attributes['available']).group()[:-1])
		self.seats = int(available_regex2.search(attributes['available']).group()[1:])
