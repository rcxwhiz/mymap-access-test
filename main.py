import webbrowser

# register the browser
chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# webbrowser.get('chrome').open('lego.com')

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://mymap.byu.edu')
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
username.send_keys('joshbedw')
password.send_keys('')
# password.submit()

print('done')
