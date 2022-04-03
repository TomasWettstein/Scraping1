from selenium import webdriver
'''Vamos a esperar a que cargue el html bajo una condicion'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = Service('C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=driver_path)
driver.get('https://eltiempo.es/')
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#term')))\
    .send_keys('Madrid')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.poi.poi-city')))\
    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[5]/main/div[4]/div/section[5]/section/div/article/section[1]/ul/li[2]/h2/a')))\
    .click()
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul/li[1]/ul')))
texto_columnas = driver.find_element(by=By.XPATH, value = '/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul')
texto_columnas = texto_columnas.text
tiempo_hoy = texto_columnas.split('Mañana')[1].split('Miércoles')[0].split('\n')[1:-1]

print(tiempo_hoy)

horas = list()
temperatura = list()
viento = list()

for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    temperatura.append(tiempo_hoy[i+1])
    viento.append(tiempo_hoy[i+2])
dt = pd.DataFrame({'Horas': horas, 'Temperatura': temperatura, 'Viento km/h': viento})
print(dt)
dt.to_csv('Tiempo_mañana.csv', index=False)
driver.quit()
