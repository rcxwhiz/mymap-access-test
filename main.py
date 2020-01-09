from selenium import webdriver
from selenium.common import exceptions
import time
import re
from classroom import *

college_page_buffer = 5

browser = webdriver.Chrome()
browser.get('http://saasta.byu.edu/noauth/classSchedule/index.php')

college_buttons = browser.find_elements_by_class_name('collegeName')

# browser.close()

for college in college_buttons:
	college.click()
	college_courses = []
	time.sleep(college_page_buffer)
	while not college_courses:
		college_courses = browser.find_elements_by_class_name('courseItem')
		time.sleep(1)
	try:
		postfix_regex = re.compile(r'.*, ')
		prefix_regex = re.compile(r', [,;]*')
		name_postfix = postfix_regex.search(college.get_attribute('college')).group(0)
		name_prefix = prefix_regex.search(college.get_attribute('college')).group(0)
		long_college_name = name_prefix[2:] + ' ' + name_postfix[:-2]
	except AttributeError:
		long_college_name = college.get_attribute('college')

	print(college.text, '|', long_college_name)
	print(f'num of courses - {len(college_courses)}')

print('done')
