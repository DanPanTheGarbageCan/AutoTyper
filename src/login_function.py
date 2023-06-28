from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def login(school_name,email,password,driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/div[2]/ul[2]/li/a'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="autosuggest-input-"]'))).click()
    driver.find_element(By.XPATH, '//*[@id="autosuggest-input-"]').send_keys(school_name)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="autosuggest-input-"]').send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-server-root"]/div/div[2]/div[1]/a[1]'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))).send_keys(email)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(password)
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__MAIN_APP__"]/div[1]/div[3]/div[2]/div[1]/div/div[7]/div[2]/div[4]/a'))).click()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article"]/div/div[2]/div/div[1]/div/div[2]/div[3]/button'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/a[9]'))).click()