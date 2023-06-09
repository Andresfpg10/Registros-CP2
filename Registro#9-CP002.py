# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCrearunanuevacuenta():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_crearunanuevacuenta(self):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.ID, "auto").click()
    element = self.driver.find_element(By.ID, "auto")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "exampleInputEmail1").click()
    self.driver.find_element(By.ID, "exampleInputEmail1").send_keys("Tucanuser123")
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("TC123")
    self.driver.find_element(By.ID, "exampleInputEmail1").click()
    self.driver.find_element(By.ID, "exampleInputEmail1").send_keys("Tucanuser1234")
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("TC1234")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys("user71@dfgt.com")
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("usuario123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn > font > font").click()
  
