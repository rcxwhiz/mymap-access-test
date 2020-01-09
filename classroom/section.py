import re


class Section:

	def __init__(self, attributes):
		self.section_num = attributes['section num']
		self.type = attributes['type']
		self.instructor = attributes['instructor']
		self.credits = attributes['credits']
		self.term = attributes['term']
		self.days = attributes['days']
		self.start = attributes['start']
		self.end = attributes['end']
		self.loction = attributes['location']
		self.available_frac = attributes['available']
		self.waitlist = int(attributes['waitlist'])

		building_regex = re.compile(r'[a-zA-Z]+')
		self.building = building_regex.search(attributes['location']).group()

		available_regex1 = re.compile(r'[0-9]+/')
		available_regex2 = re.compile(r'/[0-9]+')
		self.available = int(available_regex1.search(attributes['available']).group(1)[:-1])
		self.seats = int(available_regex2.search(attributes['available']).group(2)[1:])
