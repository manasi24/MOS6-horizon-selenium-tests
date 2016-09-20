import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
#driver.implicitly_wait(30)
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

driver.get(base_url + "project/data_processing/cluster_templates/")
driver.implicitly_wait(3)

create_cluster_template_button = driver.find_element_by_id("cluster_templates__action_create")
create_cluster_template_button.click()

plugin_name = Select(driver.find_element_by_id("id_plugin_name"))
plugin_name.select_by_value("vanilla")

vanilla_version = Select(driver.find_element_by_id("id_vanilla_version"))
vanilla_version.select_by_value("2.4.1")

create_template_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_template_button.click()

#details_group_button = driver.find_element_by_css_selector("a[data-target='#configure_cluster_template__generalconfigaction']")
#details_group_button.click()

cluster_template_name = driver.find_element_by_id("id_cluster_template_name")
cluster_template_name.send_keys("cluster-template")

anti_affinity_namenode = driver.find_element_by_id("id_anti_affinity_0")
anti_affinity_namenode.click()

anti_affinity_datanode = driver.find_element_by_id("id_anti_affinity_1")
anti_affinity_datanode.click()

anti_affinity_secondarynamenode = driver.find_element_by_id("id_anti_affinity_2")
anti_affinity_secondarynamenode.click()

node_groups_button = driver.find_element_by_css_selector("a[data-target='#configure_cluster_template__configurenodegroupsaction']")
node_groups_button.click()

select_master1 = Select(driver.find_element_by_id("template_id"))
select_master1.select_by_visible_text("master1-ngt")

add_master1_node = driver.find_element_by_id("add_group_button")
add_master1_node.click()

select_master2 = Select(driver.find_element_by_id("template_id"))
select_master2.select_by_visible_text("master2-ngt")

add_master2_node = driver.find_element_by_id("add_group_button")
add_master2_node.click()

select_slave = Select(driver.find_element_by_id("template_id"))
select_master.select_by_visible_text("slave-ngt")

add_slave_node = driver.find_element_by_id("add_group_button")
add_slave_node.click()

count_slave = driver.find_element_by_id("count_1")
count_slave.clear()
count_slave.send_keys("3")

create_ct_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_ct_button.click()

signout_button = driver.find_element_by_link_text("Sign Out")
signout_button.click()
driver.quit()
