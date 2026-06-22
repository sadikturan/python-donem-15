import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = os.path.abspath("kurs.html")
driver.get(file_path)

time.sleep(2)

cards = driver.find_elements(By.CSS_SELECTOR, ".course-card")
cards[0].click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(2)

user_input = driver.find_element(By.ID, "username")
user_input.send_keys("Selenium Kullanıcısı")
time.sleep(2)

btn = driver.find_element(By.ID, "submit-btn")
btn.click()
time.sleep(2)
driver.switch_to.alert.accept()

user_input.clear()
time.sleep(2)

user_input.send_keys("sadikturan")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("123456")
time.sleep(2)
btn.click()
driver.switch_to.alert.accept()

time.sleep(2)

driver.quit()
# class => "."
# id => "#"
# tag => "tagname"