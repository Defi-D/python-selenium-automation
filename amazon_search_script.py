from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='\Users\Dtop2\Desktop\Git Lesson\Jobeasy\python-selenium-automation\chromedriver.exe)
driver.get('https://www.amazon.com/')

driver find_element(By,ID,"twotabsearchtextbox').send_keys('coffee')

driver find_element(By,ID,"nav-search-submit-button').click()
