from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

from utilities import take_screenshot

driver = webdriver.Edge(executable_path='drivers/msedgedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://localhost:4200/login")

###############################################
# Pantalla de inicio
###############################################

username= driver.find_element_by_id('email')
username.clear()
username.send_keys("atuny0")

password= driver.find_element_by_id('password')
password.clear()
password.send_keys("9uQFF1Lh")

buton = driver.find_element_by_id('Aceptar')
buton.click()

time.sleep(2)

###############################################
# Formulario de ventas
###############################################

crearVentaLink = driver.find_element_by_id('crear-venta-link')
crearVentaLink.click()

time.sleep(1)

codigoCliente = Select(driver.find_element_by_id('codigo_cliente'))
codigoCliente.select_by_value('C001')
time.sleep(1)

codigoAlmacen = Select(driver.find_element_by_id('codigo_almacen'))
codigoAlmacen.select_by_value('A001')
time.sleep(1)

condicionPago = Select(driver.find_element_by_id('codigo_condicion_pago'))
condicionPago.select_by_value('CP001')
time.sleep(1)

tipoEntrega = Select(driver.find_element_by_id('tipo_entrega'))
tipoEntrega.select_by_value('CP002')
time.sleep(1)

agregarProducto = driver.find_element_by_id('agregar-producto')
agregarProducto.click()
time.sleep(1)

precioInput = driver.find_element_by_id('precio-input')
precioInput.send_keys('235')
time.sleep(1)

selectProducto = Select(driver.find_element_by_id('productItem'))
selectProducto.select_by_value('7')
time.sleep(1)

cantidadInput = driver.find_element_by_id('cantidad-input')
cantidadInput.send_keys('1')

subtotalInput = driver.find_element_by_id('subtotal-input')
subtotalInput.send_keys('1')

descuentoInput = driver.find_element_by_id('descuento-input')
descuentoInput.send_keys('1')
take_screenshot(driver, 'ventas', 'Formulario llenado')
time.sleep(2)
registrarVenta = driver.find_element_by_id('registrar-button')
registrarVenta.click()
take_screenshot(driver, 'ventas', 'Lista de ventas con la venta guardada')
time.sleep(5)

###############################################
# Formulario de ventas sin productos
###############################################

crearVentaLink = driver.find_element_by_id('crear-venta-link')
crearVentaLink.click()

time.sleep(1)

codigoCliente = Select(driver.find_element_by_id('codigo_cliente'))
codigoCliente.select_by_value('C002')
time.sleep(1)

codigoAlmacen = Select(driver.find_element_by_id('codigo_almacen'))
codigoAlmacen.select_by_value('A002')
time.sleep(1)

condicionPago = Select(driver.find_element_by_id('codigo_condicion_pago'))
condicionPago.select_by_value('CP002')
time.sleep(1)

tipoEntrega = Select(driver.find_element_by_id('tipo_entrega'))
tipoEntrega.select_by_value('CP002')
take_screenshot(driver, 'ventas', 'Formulario llenado sin productos')
time.sleep(5)

try:
    registrarVenta = driver.find_element_by_id('registrar-button')
    registrarVenta.click()
    time.sleep(2)
except:
    pass

listarVentas = driver.find_element_by_id('listar-ventas-link')
listarVentas.click()
take_screenshot(driver, 'ventas', 'Lista de ventas sin la venta guardada')
time.sleep(3)
driver.close()