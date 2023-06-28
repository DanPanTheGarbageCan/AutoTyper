from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import keyboard

def type(driver):
    try:
        single_char = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'token_unit._clr')))
        try:
            single_char.find_element(By.CLASS_NAME, '_enter')
            keyboard.write('\n', delay=0.055)
        except:
            keyboard.write(single_char.text, delay=0.055)
    except:
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div/button[2]')))
        next_button.click()
