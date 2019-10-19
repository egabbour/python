#pyhton
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://192.168.0.1/")
elem = driver.find_element_by_xpath('//input[@id="userName"]')
elem.send_keys("admin")