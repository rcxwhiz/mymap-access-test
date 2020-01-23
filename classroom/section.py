import datetime
import logging
import re
import sys

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
		self.location = attributes['location']
		self.available_frac = attributes['available']
		try:
			self.waitlist = int(attributes['waitlist'])
		except ValueError:
			self.waitlist = attributes['waitlist']

		self.schedule = []
		for i, meeting in enumerate(self.days):
			try:
				start_time_string = self.start[i]
				end_time_string = self.end[i]
			except IndexError:
				start_time_string = ''
				end_time_string = ''
			if start_time_string == '':
				start_time = 0
			elif ':' in start_time_string:
				start_time = datetime.datetime.strptime(start_time_string, '%I:%M %p')
			else:
				start_time = datetime.datetime.strptime(start_time_string, '%I %p')
			if end_time_string == '':
				end_time = 0
			elif ':' in end_time_string:
				end_time = datetime.datetime.strptime(end_time_string, '%I:%M %p')
			else:
				end_time = datetime.datetime.strptime(end_time_string, '%I %p')

			if start_time != 0:
				start_time = start_time.hour * 60 + start_time.minute
			if end_time != 0:
				end_time = end_time.hour * 60 + end_time.minute
			for j, day in enumerate(meeting):
				if day == 'h' or day == 'a':
					continue
				elif day == 'T':
					if j < len(meeting) - 1:
						if meeting[j + 1] == 'h':
							self.schedule.append(['Th', start_time, end_time])
						else:
							self.schedule.append(['T', start_time, end_time])
					else:
						self.schedule.append(['T', start_time, end_time])
				elif day == 'M':
					self.schedule.append(['M', start_time, end_time])
				elif day == 'W':
					self.schedule.append(['W', start_time, end_time])
				elif day == 'F':
					self.schedule.append(['F', start_time, end_time])
				elif day == 'S':
					self.schedule.append(['Sa', start_time, end_time])

		building_regex = re.compile(r'[a-zA-Z]*')
		self.building = building_regex.search(attributes['location']).group()

		available_regex1 = re.compile(r'[0-9]+/')
		available_regex2 = re.compile(r'/[0-9]+')
		try:
			self.available = int(available_regex1.search(attributes['available']).group()[:-1])
		except AttributeError:
			print(f'for some reason {attributes["available"]} isn\'t passing the regex')
			sys.exit()
		self.seats = int(available_regex2.search(attributes['available']).group()[1:])
