from openpyxl import load_workbook
from selenium import webdriver
import time
import xlwt

start = time.time()
driver = webdriver.Chrome()
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

#initialize accordingly
school_number = 0000
center_number = 0000
roll_number = 000000
max_roll_number = 000000

j = 0 #ignore
for i in range(max_roll_number):
	driver.get('http://cbseresults.nic.in/class12zpq/class12th18.htm')  #12th result webpage
	time.sleep(1.5)  #select wait time as per your internet speed
	roll_box = driver.find_element_by_name("regno").send_keys(roll_number)    
	school_box = driver.find_element_by_name("sch").send_keys(school_number)
	center_box = driver.find_element_by_name("cno").send_keys(center_number)
	submit_button = driver.find_element_by_name("B2")
	submit_button.click()
	name = driver.find_element_by_xpath("/html/body/div[1]/table[1]/tbody/tr[2]/td[2]/font/b").text
	sheet1.write(i,0,name)
	for i in range(2,7):
		subject = driver.find_element_by_xpath("/html/body/div[1]/div/center/table/tbody/tr[" + str(i) + "]/td[2]/font").text
		marks = driver.find_element_by_xpath("/html/body/div[1]/div/center/table/tbody/tr[" +str(i) + "]/td[5]/font").text
		sheet1.write(j,2*(i-2)+i,subject)  # writes, leaves one column after each subject-mark pair.
		sheet1.write(j,2*(i-2)+i+1,marks)
	j += 1
	book.save("file_name.xls")
	roll_number += 1
driver.quit() #closes chromedriver
end = time.time() 
print("Time elapsed in (s): ", end - start)
