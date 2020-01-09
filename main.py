from selenium import webdriver
from selenium import common
import time

browser = webdriver.Chrome()
browser.get('https://mymap.byu.edu')
# just have the user login themselves

register_button = None
while register_button is None:
	try:
		register_button = browser.find_element_by_id('NAVregister')
	except common.exceptions.NoSuchElementException:
		time.sleep(1)

register_button.click()

add_button = None
while add_button is None:
	try:
		add_button = browser.find_element_by_id('add-class buttonAlt')
	except common.exceptions.NoSuchElementException:
		time.sleep(1)

add_button.click()

print('done')
