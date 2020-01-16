import datetime
import re


class Semester:

	def __init__(self, attributes):
		self.timestamp = attributes['timestamp']
		self.datestamp = datetime.datetime.fromtimestamp(self.timestamp).strftime('%b-%d-%y %I:%M:%S')
		self.courses = attributes['courses']
		self.semester_year = attributes['semester year']

		semester_regex = re.compile(r'[a-zA-Z]+')
		year_regex = re.compile(r'[0-9]+')
		self.semester = semester_regex.search(self.semester_year).group()
		self.year = int(year_regex.search(self.semester_year).group())

		self.is_term = self.semester_year == 'Spring' or self.semester == 'Summer'
