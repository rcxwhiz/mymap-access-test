from my_logger import logging


class Course:

	def __init__(self, attributes):
		logging.debug('Creating a new course')
		self.short_title = attributes['short title']
		self.num = attributes['num']
		self.dept = attributes['dept']
		self.long_title = attributes['long title']
		self.description = attributes['description']
		self.college_short = attributes['college short']
		self.college_long = attributes['college long']
		self.hours = attributes['hours']
		self.offered = attributes['offered']
		self.headers = attributes['headers']
		self.note = attributes['note']
		self.when_taught = attributes['when taught']
		self.sections = attributes['sections']
		self.prerequisites = attributes['prerequisites']

		self.level = int(self.num / 100) * 100
