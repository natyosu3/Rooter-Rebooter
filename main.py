from config.password import *
from config.config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1280,768')
driver = Chrome(options=options)
driver.implicitly_wait(3)

driver.get(ROOTER_URL)

WebDriverWait(driver, 10)
password_box = driver.find_element(by=By.NAME, value="airstation_pass")
WebDriverWait(driver, 10)
password_box.send_keys(ROOTER_PASSWORD)

WebDriverWait(driver, 10)
login_btn = driver.find_element(by=By.CLASS_NAME, value="button_login")
WebDriverWait(driver, 10)
login_btn.click()
WebDriverWait(driver, 10)
setting_panel = driver.find_element(by=By.ID, value="panel_ADVANCED")
WebDriverWait(driver, 10)
setting_panel.click()
WebDriverWait(driver, 10)
driver.get(ADVANCED_PAGE)
WebDriverWait(driver, 10)
element = driver.find_element(by=By.ID, value="content_main")
WebDriverWait(driver, 10)
driver.switch_to.frame(element)

element = driver.find_element(by=By.NAME, value='reboot')
element.click()

input()