from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

base_url = "http://xx.yyy.zzz.www/horizon/"

driver.get(base_url)
print driver.title
driver.implicitly_wait(3)

username = driver.find_element_by_id("id_username")
username.send_keys("username")
password = driver.find_element_by_id("id_password")
password.send_keys("password")
password.send_keys(Keys.RETURN)
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()
signout_button = driver.find_element_by_link_text("Sign Out")
signout_button.click()
driver.implicitly_wait(7)
driver.quit()
