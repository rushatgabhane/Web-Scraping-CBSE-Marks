from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://cbseresults.nic.in/class12zpq/class12th18.htm')

filepath = 'marks.txt'
school_number = '72511'
center_number = '8801'

f = open('marks.txt', 'r')
x = f.read().splitlines()

roll_box = driver.find_element_by_name("regno")
user.click()

school_box = driver.find_element_by_name("sch")

center_box = driver.find_element_by_name("cno")

sumbmit_button = driver.find_element_by_name("B2")
