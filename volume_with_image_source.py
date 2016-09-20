import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

base_url = "http://xx.yyy.zzz.ww/horizon/"

driver.get(base_url)
print driver.title
driver.implicitly_wait(3)

#assert "Jio" in driver.title
username = driver.find_element_by_id("id_username")
username.send_keys("username")
password = driver.find_element_by_id("id_password")
password.send_keys("password")
password.send_keys(Keys.RETURN)
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

driver.get(base_url + "project/volumes/")

create_new_volume_button = driver.find_element_by_id("volumes__action_create")
create_new_volume_button.click()

volume_name = driver.find_element_by_id("id_name")
volume_name.send_keys("Volume1")

volume_source = Select(driver.find_element_by_id("id_volume_source_type"))
volume_source.select_by_value("image_source")

image_source = Select(driver.find_element_by_id("id_image_source"))
# Ubuntu14.04
#image_source.select_by_visible_text("Ubuntu14.04 (1.6 GB)")
image_source.select_by_visible_text("Windows-Server-2012-R2 (21.1 GB)")

volume_size = driver.find_element_by_id("id_size")
volume_size.clear()
volume_size.send_keys("100")

create_volume = driver.find_element_by_css_selector("input[value='Create Volume'][type='submit']")
create_volume.click()
time.sleep(10)
driver.refresh()
start = time.time()

try:
    wait = WebDriverWait(driver, 500)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/div/div/form/table/tbody/tr[1]/td[5]"),'Available'))
    wait = WebDriverWait(driver, 7)
    done = time.time()
    elapsed = done - start
    print "time taken to create 100GB volume: " + str(elapsed)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//table/tbody/tr[1]/td[1]/input')))
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/div/form/table/tbody/tr[1]/td[1]/input")
    element.click()
    delete_volume_button = driver.find_element_by_id("volumes__action_delete")
    delete_volume_button.click()
    confirm = driver.find_element_by_css_selector("a[href='#'].btn.btn-primary")
    confirm.click()
finally:
    time.sleep(5)
    signout_button = driver.find_element_by_link_text("Sign Out")
    signout_button.click()
    driver.quit()
