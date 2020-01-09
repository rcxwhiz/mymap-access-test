import re


class Course:

	def __init__(self, attributes):
		self.short_title = attributes['short title']
		self.long_title = attributes['long title']
		self.description = attributes['description']
		self.college = attributes['college']
		self.hours = attributes['hours']
		self.offered = attributes['offered']
		self.headers = attributes['headers']
		self.note = attributes['note']
		self.when_taught = attributes['when taught']
		self.sections = attributes['sections']

		num_regex = re.compile(r'[0-9]+')
		self.num = int(num_regex.search(self.short_title).group())
		self.level = int(self.num / 100) * 100

		dept_regex = re.compile(r'[a-zA-Z]+')
		self.dept = dept_regex.search(self.short_title).group()
