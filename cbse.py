from openpyxl import load_workbook
from selenium import webdriver
import time
import xlwt

start = time.time()
driver = webdriver.Chrome()
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Python Sheet 1")

#initialize accordingly
school_number = 0000
center_number = 0000
roll_number = 000000
max_roll_number = 000000

j = 0 #ignore
for i in range(max_roll_number):
	driver.get('http://cbseresults.nic.in/class12zpq/class12th18.htm')
	time.sleep(1.5)  #select wait time as per your internet speed
	roll_box = driver.find_element_by_name("regno").send_keys(roll_number)
	school_box = driver.find_element_by_name("sch").send_keys(school_number)
	center_box = driver.find_element_by_name("cno").send_keys(center_number)
	sumbmit_button = driver.find_element_by_name("B2")
	sumbmit_button.click()
	name = driver.find_element_by_xpath("/html/body/div[1]/table[1]/tbody/tr[2]/td[2]/font/b").text
	sheet1.write(i,0,name)
	for i in range(2,7):
		sub = driver.find_element_by_xpath("/html/body/div[1]/div/center/table/tbody/tr[" + str(i) + "]/td[2]/font").text
		marks = driver.find_element_by_xpath("/html/body/div[1]/div/center/table/tbody/tr[" +str(i) + "]/td[5]/font").text
		sheet1.write(j,2*(i-2)+i,sub)
		sheet1.write(j,2*(i-2)+i+1,marks)
	j += 1
	book.save("test.xls")
	roll_number += 1
driver.quit()
end = time.time()
print("Time elapsed (s): ", end - start)
