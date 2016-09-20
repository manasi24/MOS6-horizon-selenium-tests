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

username = driver.find_element_by_id("id_username")
username.send_keys("username")
password = driver.find_element_by_id("id_password")
password.send_keys("password")
password.send_keys(Keys.RETURN)
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

driver.get(base_url + "project/volumes/")
i=0
for i in range(1,11):
    create_new_volume_button = driver.find_element_by_id("volumes__action_create")
    create_new_volume_button.click()

    volume_name = driver.find_element_by_id("id_name")
    volume_name.send_keys("Volume"+str(i))
	
    volume_source = Select(driver.find_element_by_id("id_volume_source_type"))
    volume_source.select_by_value("no_source_type")

    volume_size = driver.find_element_by_id("id_size")
    volume_size.clear()
    volume_size.send_keys("1")

    create_volume = driver.find_element_by_css_selector("input[value='Create Volume'][type='submit']")
    create_volume.click()
    time.sleep(2)
    print "creation of volume" + str(i) + "successful"
    driver.refresh()
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/div/div/form/table/tbody/tr[1]/td[5]"),'Available'))
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//table/tbody/tr[1]/td[1]/input')))
    j=0
    for j in range(1,11):
	time.sleep(2)
        selector = "form > table > tbody > tr[data-display='" + "Volume" + str(j) + "'] > td.multi_select_column > input"
        element = driver.find_element_by_css_selector(selector)
        element.click()
    delete_volume_button = driver.find_element_by_id("volumes__action_delete")
    delete_volume_button.click()
    confirm = driver.find_element_by_css_selector("a[href='#'].btn.btn-primary")
    confirm.click()
except:
    print "Deletion Failed"
finally:
    time.sleep(5)
    signout_button = driver.find_element_by_link_text("Sign Out")
    signout_button.click()
    driver.quit()
