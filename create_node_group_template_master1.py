import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

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

driver.get(base_url + "project/data_processing/nodegroup_templates/")
driver.implicitly_wait(3)

create_node_group_template_button = driver.find_element_by_id("nodegroup_templates__action_create")
create_node_group_template_button.click()

plugin_name = Select(driver.find_element_by_id("id_plugin_name"))
plugin_name.select_by_value("vanilla")

vanilla_version = Select(driver.find_element_by_id("id_vanilla_version"))
vanilla_version.select_by_value("2.4.1")

create_template_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_template_button.click()

nodegroup_name = driver.find_element_by_id("id_nodegroup_name")
nodegroup_name.send_keys("master1-ngt")

flavor = Select(driver.find_element_by_id("id_flavor"))
#m1.medium
flavor.select_by_value("3f2dbfb6-89a0-4e9c-abae-d0168b0d884d")

availability_zone = Select(driver.find_element_by_id("id_availability_zone"))
availability_zone.select_by_value("Mumbai_AZ1")

storage = Select(driver.find_element_by_id("id_storage"))
storage.select_by_value("cinder_volume")

volumes_per_node = driver.find_element_by_id("id_volumes_per_node")
volumes_per_node.clear()
volumes_per_node.send_keys("1")

volumes_size = driver.find_element_by_id("id_volumes_size")
volumes_size.clear()
volumes_size.send_keys("10")

floating_ip_pool = Select(driver.find_element_by_id("id_floating_ip_pool"))
floating_ip_pool.select_by_value("85b4c3bb-ef46-4bb3-b468-a98cece7723b")

process_namenode = driver.find_element_by_id("id_processes_0")
process_namenode.click()

process_oozie = driver.find_element_by_id("id_processes_3")
process_oozie.click()

process_resourcemanager = driver.find_element_by_id("id_processes_4")
process_resourcemanager.click()

process_historyserver = driver.find_element_by_id("id_processes_6")
process_historyserver.click()

create_ngt_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_ngt_button.click()

time.sleep(10)

signout_button = driver.find_element_by_link_text("Sign Out")
signout_button.click()
driver.quit()
