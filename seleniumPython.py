from selenium import webdriver
'''Vamos a esperar a que cargue el html bajo una condicion'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
'''Opciones de navegación'''
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = Service('C:\\Users\\tomas\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
driver = webdriver.Chrome(service=driver_path)
'''Inicializamos el navegador'''
driver.get('https://eltiempo.es/')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#term')))\
    .send_keys('Madrid')

