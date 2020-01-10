from my_logger import logging


class Course:

	def __init__(self, attributes):
		logging.info('Creating a new course')
		self.short_title = attributes['dept'] + ' ' + attributes['num']
		self.num = attributes['num']
		self.dept = attributes['dept']
		self.long_title = attributes['long title']
		self.description = attributes['description']
		self.college_short = attributes['college short']
		self.college_long = attributes['college long']
		self.hours = attributes['courseCredits']
		self.offered = attributes['courseOffered']
		self.headers = attributes['courseHeaders']
		self.note = attributes['courseNote']
		self.when_taught = attributes['courseWhenTaught']
		self.prerequisites = attributes['coursePrereqs']
		self.recommended = attributes['courseRec']
		self.sections = attributes['sections']

		self.level = int(self.num[0]) * 100
		self.num_sections = len(self.sections)
