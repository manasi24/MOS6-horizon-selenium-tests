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

driver.get(base_url + "project/data_processing/clusters/")
driver.implicitly_wait(3)

create_cluster_template_button = driver.find_element_by_id("clusters__action_create")
create_cluster_template_button.click()

plugin_name = Select(driver.find_element_by_id("id_plugin_name"))
plugin_name.select_by_value("vanilla")

vanilla_version = Select(driver.find_element_by_id("id_vanilla_version"))
vanilla_version.select_by_value("2.4.1")

create_cluster_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_cluster_button.click()

cluster_name = driver.find_element_by_id("id_cluster_name")
cluster_name.send_keys("cluster1")

select_cluster_template = Select(driver.find_element_by_id("id_cluster_template"))
select_cluster_template.select_by_visible_text("cluster-template")

base_image = Select(driver.find_element_by_id("id_image"))
base_image.select_by_value("99c75ab0-d2f9-4a93-a567-3625e2d5bdf5")

keypair = Select(driver.find_element_by_id("id_keypair"))
keypair.select_by_value("cloud-qa")

mgmt_network = Select(driver.find_element_by_id("id_neutron_management_network"))
mgmt_network.select_by_value("c18c273b-832e-410e-9857-fbb59927955a")

launch_cluster = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
launch_cluster.click()

try:
    wait = WebDriverWait(driver, 300)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/div/form/table/tbody/tr/td[3]"),'Active'))
finally:
    time.sleep(5)
    signout_button = driver.find_element_by_link_text("Sign Out")
    signout_button.click()
    driver.quit()
