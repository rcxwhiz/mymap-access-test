import re
import threading
import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select

from classroom import *


def get_college_buttons(browser, delay=0.2, max_wait=2.0):
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
			print('Ran out of time getting college buttons without encountering stale elements, passing what was given.\n'
			      'This is probably not an issue')
			return college_buttons


def get_semester(semester_year, recheck_delay=0.1):
	start = time.time()
	print(f'Getting a semester {semester_year}')

	semester_attributes = {'timestamp': time.time(),
	                       'semester year': semester_year,
	                       'courses': []}

	semester_to_return = Semester(semester_attributes)

	browser = webdriver.Chrome()
	browser.get('http://saasta.byu.edu/noauth/classSchedule/index.php')
	semester_button = Select(browser.find_element_by_id('yearterm'))
	try:
		semester_button.select_by_visible_text(semester_year)
	except exceptions.NoSuchElementException:
		print(f'ERROR - Semester {semester_year} not found')
		browser.close()
		return None

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
			print('Found a stale element :( this should not have happened')
			return None
		colleges.append({'short name': college.text, 'long name': long_college_name})
	browser.close()

	# Will open 1 - the number here of browser windows
	MAX_NUM_THREADS = 100

	threads = []
	for college in colleges:
		while threading.active_count() >= MAX_NUM_THREADS:
			time.sleep(5)

		th = threading.Thread(target=get_college, args=(semester_year, college, semester_to_return.courses))
		threads.append(th)
		th.start()

	for thread in threads:
		thread.join()

	diff = time.time() - start
	print(f'spent {diff / 60:.0f}:{diff % 60:.0f} getting {semester_year}')
	return semester_to_return


def get_college(semester_year, college, semester_course_list):
	print(f'opening a window for {college["short name"]}')
	browser = webdriver.Chrome()
	browser.get('http://saasta.byu.edu/noauth/classSchedule/index.php')
	semester_button = Select(browser.find_element_by_id('yearterm'))
	semester_button.select_by_visible_text(semester_year)
	college_buttons = get_college_buttons(browser)

	for college_button in college_buttons:
		if college_button.text == college['short name']:
			college_button.click()
			break

	time.sleep(2)
	completed_courses = []
	course_buttons = browser.find_elements_by_class_name('courseItem')
	while True:
		try:
			for course_loop in course_buttons:
				test = course_loop.text
			break
		except exceptions.StaleElementReferenceException:
			course_buttons = browser.find_elements_by_class_name('courseItem')

	total_courses = []
	for course_button in course_buttons:
		total_courses.append(course_button.text)

	for current_course in total_courses:
		while True:
			response = get_course(browser, current_course, course_buttons, college)
			if response != 0:
				completed_courses.append(current_course)
				semester_course_list.append(response)
				break
			if response == 0:
				browser.close()
				browser.get('http://saasta.byu.edu/noauth/classSchedule/index.php')
				semester_button = Select(browser.find_element_by_id('yearterm'))
				semester_button.select_by_visible_text(semester_year)
				college_buttons = get_college_buttons(browser)

				for college_button in college_buttons:
					if college_button.text == college['short name']:
						college_button.click()
						break

				course_buttons = browser.find_elements_by_class_name('courseItem')

	browser.close()
	print(f'closing a window for {college["short name"]}')


def get_course(browser, course_name_in, college_course_buttons, college):
	checks = 0
	for course_button in college_course_buttons:
		if course_button.text == course_name_in:
			course_button.click()
			while True:
				course_attributes = {'college short': college['short name'],
				                     'college long': college['long name'],
				                     'dept': browser.find_element_by_id('courseDept').text,
				                     'num': browser.find_element_by_id('courseNumber').text}
				if '' not in course_attributes.values() and None not in course_attributes.values():
					break
				if checks > 50:
					return 0
				time.sleep(0.1)

			course_attributes['long title'] = browser.find_element_by_id('courseTitle').text
			course_attributes['description'] = browser.find_element_by_id('courseDescription').text
			course_attributes['sections'] = []
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

			sections = browser.find_elements_by_class_name('match')

			section_counter = 0
			for section_data in sections:
				section_counter += 1

				# use the data we get from a section to create the object and add it to the course
				data = section_data.find_elements_by_tag_name('td')
				section_attributes = {'section num': data[0].text,
				                      'type': data[1].text,
				                      'instructor': data[2].text,
				                      'credits': data[3].text,
				                      'term': data[4].text,
				                      'days': data[5].text.split('\n'),
				                      'starts': data[6].text.split('\n'),
				                      'ends': data[7].text.split('\n'),
				                      'location': data[8].text,
				                      'available': data[9].text,
				                      'waitlist': data[10].text}
				course_attributes['sections'].append(Section(section_attributes))
			return Course(course_attributes)
