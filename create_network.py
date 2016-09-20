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

driver.get(base_url + "project/networks/")

create_new_network_button = driver.find_element_by_id("networks__action_create")
create_new_network_button.click()

network_name = driver.find_element_by_id("id_net_name")
network_name.send_keys("Network1")

network_admin_state = Select(driver.find_element_by_id("id_admin_state"))
#UP
network_admin_state.select_by_value("True")

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

#time.sleep(2)
subnet_name = driver.find_element_by_id("id_subnet_name")
subnet_name.send_keys("Subnet1")

network_address = driver.find_element_by_id("id_cidr")
network_address.send_keys("10.0.0.0/24")

ip_version = Select(driver.find_element_by_id("id_ip_version"))
#IPv4
ip_version.select_by_visible_text("IPv4")

gateway_ip = driver.find_element_by_id("id_gateway_ip")
gateway_ip.send_keys("10.0.0.1")

next_button = driver.find_element_by_css_selector("button[type='button'].btn.btn-primary.button-next")
next_button.click()

create_button = driver.find_element_by_css_selector("button[type='submit'].btn.btn-primary.button-final")
create_button.click()

time.sleep(5)

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
#volume_id.select_by_visible_text("Volume1 - 10 GB (Volume)")
volume_id.select_by_index('1')

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

#net_list = self.driver.find_element_by_id("available_network")
net_list = driver.find_element_by_xpath("//body/div[3]/div/form/div/div/div[2]/div/fieldset[4]/table[1]/tbody/tr/td[1]/ul[2]/li[1]/a")
net_list.click()

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

    time.sleep(5)
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
