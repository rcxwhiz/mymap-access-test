from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select
import datetime
import time
import re
import sys
from classroom import *


def get_college_buttons(browser, delay, max_wait=2.0):
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


def get_courses_page(browser, delay, max_wait=2.0):
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
			print('Ran out of time getting courses without encountering stale elements, passing what was given.\n'
			      'This is probably not an issue.')
			return college_courses


def get(semester_year, recheck_delay=0.1):

	get_start = time.time()
	semester_attributes = {'timestamp': time.time(),
	                       'semester year': semester_year,
	                       'courses': []}

	print(f'Getting classes for {semester_year}')
	print('this may take about an hour...')

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
		colleges.append([college.text, long_college_name])

	college_counter = 0
	for college in colleges:
		college_counter += 1
		college_buttons = get_college_buttons(browser, recheck_delay)

		# find the right college button to click and click it
		for button in college_buttons:
			if button.text == college[0]:
				button.click()

		college_courses = get_courses_page(browser, recheck_delay)

		course_counter = 0
		for clicked_course in college_courses:
			course_counter += 1
			clicked_course.click()

			checks = 0
			while True:
				if checks > 50:
					print('Reloading course due to some timeout')
					browser.refresh()
					time.sleep(3)
					college_buttons = get_college_buttons(browser, recheck_delay)
					for button in college_buttons:
						if button.text == college[0]:
							button.click()
					college_courses = get_courses_page(browser, recheck_delay)
					for i, subcourse in enumerate(college_courses):
						if i + 1 == course_counter:
							break
					continue
				course_attributes = {'college short': college[0],
				                     'college long': college[1],
				                     'dept': browser.find_element_by_id('courseDept').text,
				                     'num': browser.find_element_by_id('courseNumber').text}
				to_break = True
				for value in course_attributes.values():
					if not value:
						to_break = False
				if to_break:
					break
				checks += 1
				time.sleep(recheck_delay)
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
				# printing progress here
				update_string = f'\r[{str(datetime.timedelta(seconds=int(time.time() - get_start)))}]'
				update_string += f' College {college_counter}/{len(colleges)} ({college_counter / len(colleges) * 100:.0f}%)'
				update_string += f' - Course {course_counter}/{len(college_courses)} ({course_counter / len(college_courses) * 100:.0f}%)'
				update_string += f' - Section {section_counter}/{len(sections)} ({section_counter / len(sections) * 100:.0f}%)'
				update_string += ' ' * 10
				sys.stdout.write(update_string)
				sys.stdout.flush()

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

			semester_attributes['courses'].append(Course(course_attributes))

		browser.refresh()
		semester_button = Select(browser.find_element_by_id('yearterm'))
		semester_button.select_by_visible_text(semester_year)

	browser.close()
	semester_out = Semester(semester_attributes)
	print(f'Finished getting classes for {semester_year}')
	return semester_out
