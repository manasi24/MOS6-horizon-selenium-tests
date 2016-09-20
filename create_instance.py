import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

driver.get(base_url + "project/volumes/")

create_new_volume_button = driver.find_element_by_id("volumes__action_create")
create_new_volume_button.click()

volume_name = driver.find_element_by_id("id_name")
volume_name.send_keys("Volume1")

volume_source_type = Select(driver.find_element_by_id("id_volume_source_type"))
volume_source_type.select_by_value("image_source")

image_source = Select(driver.find_element_by_id("id_image_source"))
# Ubuntu14.04
image_source.select_by_value("50639106-509f-4c20-af8a-c5aa593f5789")

volume_size = driver.find_element_by_id("id_size")
volume_size.clear()
volume_size.send_keys("10")

create_volume = driver.find_element_by_css_selector("input[value='Create Volume'][type='submit']")
create_volume.click()

try:
    wait = WebDriverWait(driver, 140)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/div/div/form/table/tbody/tr[1]/td[5]"),'Available'))
finally:
    pass

driver.get(base_url + "project/instances/")

create_instance_button = driver.find_element_by_id("instances__action_launch")
create_instance_button.click()

time.sleep(2)

availability_zone = Select(driver.find_element_by_id("id_availability_zone"))
availability_zone.select_by_value("Mumbai_AZ1")

instance_name = driver.find_element_by_id("id_name")
instance_name.send_keys("Instance1")

instance_source_type = Select(driver.find_element_by_id("id_source_type"))
instance_source_type.select_by_value("volume_id")

volume_id = Select(driver.find_element_by_id("id_volume_id"))
volume_id.select_by_visible_text("Volume1 - 10 GB (Volume)")

delete_on_terminate = driver.find_element_by_id("id_delete_on_terminate")
delete_on_terminate.click()

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

time.sleep(2)

flavor = Select(driver.find_element_by_id("id_flavor"))
#m1.small
flavor.select_by_value("7b26c432-f7cf-4b8c-80c6-19a93cdaab6e")

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

time.sleep(2)

keypair = Select(driver.find_element_by_id("id_keypair"))
keypair.select_by_value("cloud-qa")

#default_security_group = driver.find_element_by_id("id_groups_0")
#default_security_group.deselect()
#default_security_group.click()

allow_all_security_group = driver.find_element_by_id("id_groups_1")
#allow_all_security_group = driver.find_element_by_link_text(" Allow All")
allow_all_security_group.click()

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

time.sleep(2)

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

time.sleep(2)

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

time.sleep(2)

submit_button = driver.find_element_by_css_selector("button[type='submit'].btn.btn-primary.button-final")
submit_button.click()

try:
    time.sleep(5)
    wait = WebDriverWait(driver, 150)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/form/table/tbody/tr[1]/td[9]"),'Active'))
    time.sleep(2)
    #floating ip            
    selector = "form > table > tbody > tr[data-display=" + "Instance1" + "] > td.actions_column > div > a:nth-child(2)"
    action_list = driver.find_element_by_css_selector(selector)
    action_list.click()
    time.sleep(5)
    floating_ip = driver.find_element_by_link_text("Associate Floating IP")
    floating_ip.click()

    #associate floating ip
    select_floating_ip =Select(driver.find_element_by_id("id_ip_id"))

    for o in select_floating_ip.options:
        if o.text == "Select an IP address":
            select_floating_ip.select_by_index(1)
	    #o.click()
	    associate_button = driver.find_element_by_css_selector("input[type='submit'][value='Associate']")
            associate_button.click()
	    time.sleep(2)
	    break
        elif o.text == "No floating IP addresses allocated":
	    select_floating_ip.select_by_index(0)
            add_floating_ip = driver.find_element_by_xpath("//body/div[3]/div/form/div/div/div[2]/div/fieldset/table/tbody/tr/td[1]/div[1]/div/div/span/a")
            add_floating_ip.click()
	    #<input class="btn btn-primary pull-right" type="submit" value="Allocate IP">
	    time.sleep(1)
	    allocate_ip = driver.find_element_by_css_selector("input[type='submit'][value='Allocate IP']")
	    allocate_ip.click()
	    time.sleep(1)
            associate_button = driver.find_element_by_css_selector("input[type='submit'][value='Associate']")
            associate_button.click()
            time.sleep(2)
	    break

    wait = WebDriverWait(driver, 7)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//table/tbody/tr[1]/td[1]/input')))
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/form/table/tbody/tr[1]/td[1]/input")
    element.click()
    delete_volume_button = driver.find_element_by_id("instances__action_terminate")
    delete_volume_button.click()
    confirm = driver.find_element_by_css_selector("a[href='#'].btn.btn-primary")
    confirm.click()
finally:
    time.sleep(8)
    signout_button = driver.find_element_by_link_text("Sign Out")
    signout_button.click()
    driver.quit()
