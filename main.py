from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select
import time
import re
import sys
from classroom import *

college_page_buffer = 5

browser = webdriver.Chrome()
browser.get('http://saasta.byu.edu/noauth/classSchedule/index.php')
# browser.close()

semester = 'Fall 2019'
semester_button = Select(browser.find_element_by_id('yearterm'))
try:
	semester_button.select_by_visible_text(semester)
except exceptions.NoSuchElementException:
	sys.exit('ERROR - Semester not found')

college_buttons = browser.find_elements_by_class_name('collegeName')

for college in college_buttons:
	college.click()

	# get list of courses from that college
	college_courses = []
	time.sleep(college_page_buffer)
	while not college_courses:
		college_courses = browser.find_elements_by_class_name('courseItem')
		time.sleep(1)

	# make the long name of the college
	while True:
		try:
			postfix_regex = re.compile(r'.*, ')
			prefix_regex = re.compile(r', [^,]*$')
			name_postfix = postfix_regex.search(college.get_attribute('college')).group(0)
			name_prefix = prefix_regex.search(college.get_attribute('college')).group(0)
			long_college_name = name_prefix[2:] + ' ' + name_postfix[:-2]
			break
		except AttributeError:
			long_college_name = college.get_attribute('college')
			break
		except exceptions.StaleElementReferenceException:
			print('Found a stale element')

	# print the college names and number of courses
	print(f'{college.text} | {long_college_name}')
	print(f'num of courses - {len(college_courses)}')

print('done')
