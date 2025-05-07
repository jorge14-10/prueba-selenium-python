from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from faker import Faker
import random

class Caso1Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def cargar(self, url):
        self.driver.get(url)
        title = self.driver.title
        assert title == "avianca - encuentra tiquetes y vuelos baratos | Web oficial", f"Título incorrecto: se obtuvo '{title}'"
    
    def seleccionar_solo_ida(self):
        solo_ida = self.driver.find_element(By.ID, "journeytypeId_1")
        solo_ida.click()
    
    def seleccionar_origen(self, origen):
        origen_padre = self.driver.find_element(By.ID, "originDiv")
        input_origen = origen_padre.find_element(by=By.CLASS_NAME, value="control_field_input")
        origen_padre.click()
        input_origen.send_keys(origen)

        select_origen = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='station-control-list_item_link']"))
        )
        select_origen.click()

    def seleccionar_destino(self):
        lista_destino = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='arrivalStationsListId']//li"))
        )
        actions = ActionChains(self.driver)
        actions.click(lista_destino[1]).perform()

    def seleccionar_pasajeros(self):
        boton_pasajeros = self.driver.find_element(By.XPATH, "//div[@class='ibe-search_pax-control']//button[@class='control_field_button']")
        boton_pasajeros.click()

        lista_pasajeros = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='pax-control_selector']//li"))
        )
        agregar_pasajero_adulto = lista_pasajeros[1].find_element(By.XPATH, ".//button[@class='ui-num-ud_button plus']")
        agregar_pasajero_adulto.click()
    
    def confirmar_pasajeros(self):
        boton_de_confirmacion = self.driver.find_element(By.XPATH, "//button[@class='button control_options_selector_action_button']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", boton_de_confirmacion)
        time.sleep(1)
        boton_de_confirmacion.click()

    def buscar(self):
        boton_de_buscar = self.driver.find_element(by=By.ID, value="searchButton")
        boton_de_buscar.click()

    def seleccionar_plan(self):
        boton_desplegable = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='journey_price']"))
        )
        boton_desplegable[0].click()

        boton_plan = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='journey_fares_list_item ng-tns-c12-3 ng-star-inserted']"))
        )
        self.wait.until(EC.element_to_be_clickable(boton_plan[0]))
        boton_plan[0].click()

    def validar_summary(self):
        nombre_plan = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "journey_price_fare_name-text"))
        )

        contenedor = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "journey_price")))
        assert "basic" in contenedor.text.lower(), "El texto 'basic' no se encuentra dentro del contenedor"

    def continuar(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))

        boton_continuar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button page_button btn-action page_button-primary-flow ng-star-inserted']"))
        )
        boton_continuar.click()
