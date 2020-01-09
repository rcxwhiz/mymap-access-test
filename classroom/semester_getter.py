from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
import re
from classroom import *
from my_logger import logging


def page_loaded(browser):
	page_state = browser.execute_script('return document.readyState;')
	return page_state == 'complete'


def wait_for_page(browser, timeout=10):
	old_page = browser.find_element_by_tag_name('html')
	yield
	WebDriverWait(browser, timeout).until(EC.staleness_of(old_page))


def get(semester_year, page_load_buffer=3):

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

	# TODO find a way to wait the right amount of time for the page to load
	# time.sleep(page_load_buffer)
	WebDriverWait(browser, page_load_buffer).until(EC.element_to_be_clickable((By.CLASS_NAME, 'collegeName')))
	college_buttons = browser.find_elements_by_class_name('collegeName')

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
			logging.critical('Found a stale element :(')
			return None
		colleges.append([college.text, long_college_name])

	for college in colleges:
		college_buttons = browser.find_elements_by_class_name('collegeName')
		for button in college_buttons:
			if button.text == college[0]:
				button.click()

		# print the college names and number of courses
		logging.info(f'{college[0]} | {college[1]}')

		# get list of courses from that college
		college_courses = []
		time.sleep(page_load_buffer)
		while not college_courses:
			college_courses = browser.find_elements_by_class_name('courseItem')
			time.sleep(1)
		logging.info(f'num of courses - {len(college_courses)}')

		for course in college_courses:
			course.click()
			time.sleep(page_load_buffer)
			course_attributes = {'college short': college[0],
			                     'college long': college[1],
			                     'dept': browser.find_element_by_id('courseDept').text,
			                     'num': browser.find_element_by_id('courseNumber').text,
			                     'long title': browser.find_element_by_id('courseTitle').text,
			                     'description': browser.find_element_by_id('courseDescription').text}

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
		time.sleep(page_load_buffer)
		# here I need to find a new way to iterate through the colleges

	browser.close()
	logging.info(f'Finished getting classes for {semester_year}')
