from selenium import webdriver
import selenium.common.exceptions
from time import sleep

chrome_driver_path = "/Users/nathanj/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?geoId=90000049&keywords=python%20developer&location=Los%20Angeles%20Metropolitan%20Area")

sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
sign_in_button.click()

sleep(2)
username_form = driver.find_element_by_id("username")
password_form = driver.find_element_by_id("password")

username_form.send_keys("bobkinsville@gmail.com")
password_form.send_keys("&abc12345")

submit_button = driver.find_element_by_class_name("from__button--floating")
submit_button.click()

sleep(2)
next_applications = driver.find_elements_by_class_name("job-card-list__title")

for application in next_applications:
    sleep(2)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
    try:
        application.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        break

driver.quit()
