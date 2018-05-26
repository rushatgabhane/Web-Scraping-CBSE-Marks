from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://cbseresults.nic.in/class12zpq/class12th18.htm')

filepath = 'marks.txt'
school_number = '72511'
center_number = '8801'
rollnumber = 8100000  #to be iterated

f = open('marks.txt', 'r')
x = f.read().splitlines()

roll_box = driver.find_element_by_name("regno").send_keys(roll_number)

school_box = driver.find_element_by_name("sch").send_keys(school_number)

center_box = driver.find_element_by_name("cno").send_keys(center_number)

sumbmit_button = driver.find_element_by_name("B2")
