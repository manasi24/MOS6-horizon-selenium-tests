import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

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
select_slave.select_by_visible_text("slave-ngt")

add_slave_node = driver.find_element_by_id("add_group_button")
add_slave_node.click()

count_slave = driver.find_element_by_id("count_2")
count_slave.clear()
count_slave.send_keys("3")

create_ct_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_ct_button.click()

time.sleep(20)
create_cluster = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/table/tbody/tr[1]/td[7]/div/a[1]")
create_cluster.click()

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

create_cluster_button = driver.find_element_by_css_selector("input[value='Create'][type='submit']")
create_cluster_button.click()

try:
    wait = WebDriverWait(driver, 300)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/div/form/table/tbody/tr/td[3]"),'Active'))
    wait = WebDriverWait(driver, 7)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//table/tbody/tr/td[1]/input')))
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/table/tbody/tr/td[1]/input")
    element.click()
    delete_volume_button = driver.find_element_by_id("clusters__action_delete")
    delete_volume_button.click()
    confirm = driver.find_element_by_css_selector("a[href='#'].btn.btn-primary")
    confirm.click()

finally:
    time.sleep(5)
    signout_button = driver.find_element_by_link_text("Sign Out")
    signout_button.click()
    driver.quit()
