from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
webdriver_service = Service("C:\selenium\python\chromedriver_win32")
driver = webdriver.Chrome(service=webdriver_service)
driver.get("file:///C:/Users/MYPC/OneDrive/Desktop/Distance.html")
time.sleep(3)
driver.find_element(By.ID,"auto1").click()
time.sleep(2)
driver.find_element(By.ID,"email").send_keys('gadde.tharanmai24@gmail.com')
time.sleep(1)
driver.find_element(By.ID,"password").send_keys('bhjbjbj')
time.sleep(1)
driver.find_element(By.ID,"auto2").click()
time.sleep(2)
driver.find_element(By.ID,"origin").send_keys('Mustikuntla')
time.sleep(2)
driver.find_element(By.ID,"destination").send_keys('Hyderabad')
time.sleep(1)
driver.find_element(By.ID,"auto3").click()
time.sleep(5)
driver.find_element(By.ID,"auto4").click()
time.sleep(3)
alert=Alert(driver)
alert.accept()
time.sleep(2)
driver.close()