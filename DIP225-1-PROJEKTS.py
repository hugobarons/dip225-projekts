from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

username = 'dailyotisfan'
password = 'Dailyotisfan1!'

options = Options()
options.add_experimental_option("detach", False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)

decline_cookies_button = driver.find_element(By.XPATH, "//button[contains(., 'Decline')]")
decline_cookies_button.click()
time.sleep(2)

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys(username)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

driver.get("https://www.instagram.com/daily_otis/?hl=en")
time.sleep(3)

photo = driver.find_element(By.CSS_SELECTOR, )

actions = ActionChains(driver)
actions.double_click(photo).perform()

time.sleep(2)
driver.quit()