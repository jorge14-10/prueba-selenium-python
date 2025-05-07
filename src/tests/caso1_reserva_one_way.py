from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://nuxqa4.avtest.ink/")

title = driver.title
assert title == "avianca - encuentra tiquetes y vuelos baratos | Web oficial", f"Título incorrecto: se obtuvo '{title}'"

wait = WebDriverWait(driver, 20)

#language = driver.find_element(By.XPATH, "//ul[@class='main-header_nav-secondary_list']//div[@class='language-selector']//button[@id='languageListTriggerId_71']")
#language.click()
#language = driver.find_element(by=By.CLASS_NAME, value="language-selector")
#language.click()

#Seleccionar solo ida
solo_ida = driver.find_element(By.ID, "journeytypeId_1")
solo_ida.click()

#Seleccionar un origen
origen_padre = driver.find_element(By.ID, "originDiv")
input_origen = origen_padre.find_element(by=By.CLASS_NAME, value="control_field_input")
origen_padre.click()
input_origen.send_keys("Medellin")

select_origen = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='station-control-list_item_link']"))
)
select_origen.click()


#Seleccionar un destino
lista_destino = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='arrivalStationsListId']//li"))
)
actions = ActionChains(driver)
actions.click(lista_destino[1]).perform()

#Seleccionar pasajeros
boton_pasajeros = driver.find_element(By.XPATH, "//div[@class='ibe-search_pax-control']//button[@class='control_field_button']")
boton_pasajeros.click()

lista_pasajeros = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='pax-control_selector']//li"))
)
agregar_pasajero_adulto = lista_pasajeros[1].find_element(By.XPATH, ".//button[@class='ui-num-ud_button plus']")
agregar_pasajero_adulto.click()

#Confirmar pasajeros
boton_de_conformacion = origen_padre.find_element(By.XPATH, "//button[@class='button control_options_selector_action_button']")
boton_de_conformacion.click()

