import pickle
import os
import sys
from classroom import semester_getter
from my_logger import logging


class SemesterManager:

	def __init__(self):
		self.semesters = {}

		pickles_path = os.path.join(os.path.dirname(sys.argv[0]), 'pickles')
		if not os.path.exists(pickles_path):
			os.makedirs(pickles_path)
		os.chdir(pickles_path)

		for file in os.listdir():
			self.semesters[file] = pickle.load(open(file, 'rb'))

	def semester(self, semester_year):
		if semester_year in self.semesters.keys():
			return self.semesters[semester_year]
		logging(f'Requested semester {semester_year} not in semester manager')
		return None

	def update(self, semester_year):
		self.semesters[semester_year] = semester_getter.get(semester_year)
		if os.path.exists(semester_year):
			os.remove(semester_year)
		if self.semesters[semester_year] is not None:
			pickle.dump(self.semesters[semester_year], open(semester_year, 'wb'))

	def cached_semesters(self):
		return self.semesters.keys()
