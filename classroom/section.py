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

		# TODO put in a thing here where I make a list of all the times the section meets

		building_regex = re.compile(r'[a-zA-Z]*')
		self.building = building_regex.search(attributes['loction']).group()

		available_regex1 = re.compile(r'[0-9]+/')
		available_regex2 = re.compile(r'/[0-9]+')
		self.available = int(available_regex1.search(attributes['available']).group()[:-1])
		self.seats = int(available_regex2.search(attributes['available']).group()[1:])
