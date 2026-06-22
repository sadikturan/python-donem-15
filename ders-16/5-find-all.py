from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = os.path.abspath("kurs.html")
driver.get(file_path)


# find_elements() => çoğul
courses = driver.find_elements(By.CLASS_NAME, "course-card")
# courses = driver.find_elements(By.CSS_SELECTOR, ".course-card")

print(f"Number of courses: {len(courses)}")

for kurs in courses:
    title = kurs.find_element(By.TAG_NAME, "h2").text
    description = kurs.find_element(By.TAG_NAME, "p").text
    price = kurs.find_element(By.TAG_NAME, "span").text
    print(f"Course Title: {title}")
    print(f"Course Description: {description}")
    print(f"Course Price: {price}")
    print("-" * 20)


time.sleep(5)
driver.quit()