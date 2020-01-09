from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select
import datetime
import time
import re
from classroom import *
from my_logger import logging


def get_college_buttons(browser, delay, max_wait=3.0):
	college_buttons = browser.find_elements_by_class_name('collegeName')
	start = time.time()
	while True:
		try:
			for college in college_buttons:
				college.get_attribute('college')
			time.sleep(delay)
		except exceptions.StaleElementReferenceException:
			college_buttons = browser.find_elements_by_class_name('collegeName')
			return college_buttons
		if time.time() - start > max_wait:
			logging.info('Ran out of time without encountering stale elements, passing what was given')
			return college_buttons


def get_courses_page(browser, delay, max_wait=5.0):
	start = time.time()
	college_courses = []
	while not college_courses:
		college_courses = browser.find_elements_by_class_name('courseItem')

	while True:
		try:
			for course in college_courses:
				course.text
			time.sleep(delay)
		except exceptions.StaleElementReferenceException:
			college_courses = browser.find_elements_by_class_name('courseItem')
			return college_courses
		if time.time() - start > max_wait:
			logging.info('Ran out of time without encountering stale elements, passing what was given')
			return college_courses


def get(semester_year, page_load_buffer=3, recheck_delay=0.1):

	semester_attributes = {'timestamp': datetime.datetime,
	                       'semester year': semester_year,
	                       'courses': []}

	logging.info(f'Getting classes for {semester_year}')

	browser = webdriver.Chrome()
	browser.get('http://saasta.byu.edu/noauth/classSchedule/index.php')

	semester_button = Select(browser.find_element_by_id('yearterm'))
	try:
		semester_button.select_by_visible_text(semester_year)
	except exceptions.NoSuchElementException:
		logging.error(f'ERROR - Semester {semester_year} not found')

	college_buttons = get_college_buttons(browser, recheck_delay)

	colleges = []
	for college in college_buttons:
		try:
			postfix_regex = re.compile(r'.*, ')
			prefix_regex = re.compile(r', [^,]*$')
			name_postfix = postfix_regex.search(college.get_attribute('college')).group(0)
			name_prefix = prefix_regex.search(college.get_attribute('college')).group(0)
			long_college_name = name_prefix[2:] + ' ' + name_postfix[:-2]
		except AttributeError:
			long_college_name = college.get_attribute('college')
		except exceptions.StaleElementReferenceException:
			logging.critical('Found a stale element :( this should not have happened')
			return None
		colleges.append([college.text, long_college_name])

	for college in colleges:
		college_buttons = get_college_buttons(browser, recheck_delay)

		# find the right college button to click and click it
		for button in college_buttons:
			if button.text == college[0]:
				button.click()

		# print the college names and number of courses
		logging.info(f'{college[0]} | {college[1]}')

		college_courses = get_courses_page(browser, recheck_delay)

		for clicked_course in college_courses:
			clicked_course.click()
			# wait_for_course_load(browser, recheck_delay)
			while True:
				course_attributes = {'college short': college[0],
				                     'college long': college[1],
				                     'dept': browser.find_element_by_id('courseDept').text,
				                     'num': browser.find_element_by_id('courseNumber').text,
				                     'long title': browser.find_element_by_id('courseTitle').text,
				                     'description': browser.find_element_by_id('courseDescription').text}
				to_break = True
				for value in course_attributes.values():
					if not value:
						to_break = False
				if to_break:
					break
				time.sleep(recheck_delay)

			things_to_try = ['courseCredits',
			                 'courseOffered',
			                 'courseHeaders',
			                 'courseNote',
			                 'courseWhenTaught',
			                 'coursePrereqs',
			                 'courseRec']

			for thing in things_to_try:
				try:
					course_attributes[thing] = browser.find_element_by_id(thing).text
				except exceptions.NoSuchElementException:
					course_attributes[thing] = ''

		time.sleep(page_load_buffer)
		browser.refresh()

	browser.close()
	logging.info(f'Finished getting classes for {semester_year}')
