from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = os.path.abspath("kurs.html")
driver.get(file_path)


# find_element()   => tekil
# find_elements()  => çoğul


header = driver.find_element(By.ID, "header")
print(f"header: {header.text}")

subtitle = driver.find_element(By.TAG_NAME, "h2").text
print(f"subtitle: {subtitle.text}")

input_element = driver.find_element(By.NAME, "username")
print(f"Input Placeholder: {input_element.get_attribute('placeholder')}")

course = driver.find_element(By.CLASS_NAME, "course-card")

course_title = course.find_element(By.TAG_NAME, "h2")
course_description = course.find_element(By.TAG_NAME, "p")
course_price = course.find_element(By.TAG_NAME, "span")

print(f"Course Title: {course_title.text}")
print(f"Course Description: {course_description.text}")
print(f"Course Price: {course_price.text}")


time.sleep(5)
driver.quit()