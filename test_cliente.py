from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("http://localhost:4200/login")

###############################################
# Pantalla de inicio
###############################################

username= driver.find_element(By.ID, 'email')
username.clear()
username.send_keys("atuny0")

password= driver.find_element(By.ID, 'password')
password.clear()
password.send_keys("9uQFF1Lh")

buton = driver.find_element(By.ID, 'Aceptar')
buton.click()

time.sleep(7)

###############################################
# listado
###############################################

buton = driver.find_element(By.ID, 'listadoclientes')
buton.click()

time.sleep(7)

###############################################
# menu
###############################################

buton = driver.find_element(By.ID, 'crearcliente')
buton.click()

###############################################
# datos cliente correcto
###############################################

username= driver.find_element(By.ID, 'nombre')
username.clear()
username.send_keys("Snydher")

carnet= driver.find_element(By.ID, 'ci')
carnet.clear()
carnet.send_keys("3232323")

carnet= driver.find_element(By.ID, 'tipoDocumento')
carnet.clear()
carnet.send_keys("Carnet")

carnet= driver.find_element(By.ID, 'email')
carnet.clear()
carnet.send_keys("snydher@gmail.com")

time.sleep(7)

buton = driver.find_element(By.ID, 'grabar')
buton.click()

###############################################
# listado
###############################################

buton = driver.find_element(By.ID, 'listadoclientes')
buton.click()

time.sleep(7)

###############################################
# menu cliente incorrecto
###############################################

buton = driver.find_element(By.ID, 'crearcliente')
buton.click()

###############################################
# datos cliente
###############################################

username= driver.find_element(By.ID, 'nombre')
username.clear()
username.send_keys("Snydher")

carnet= driver.find_element(By.ID, 'ci')
carnet.clear()
carnet.send_keys("3232323")

carnet= driver.find_element(By.ID, 'tipoDocumento')
carnet.clear()
carnet.send_keys("Carnet")

carnet= driver.find_element(By.ID, 'email')
carnet.clear()
carnet.send_keys("sny.com")

time.sleep(7)

buton = driver.find_element(By.ID, 'grabar')
if buton.is_enabled():
    buton.click()
else:
    print("datos incorrectos no se grabara el registro con email incorrecto")

###############################################
# listado
###############################################

buton = driver.find_element(By.ID, 'listadoclientes')
buton.click()

time.sleep(10)


driver.quit