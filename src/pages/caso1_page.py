#Importaciones necesarias para que el page funcione
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from faker import Faker
import random

fake = Faker("es_ES")

class Caso1Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    #Recibe la url de la pagina a cargar
    def cargar(self, url):
        self.driver.get(url)
        title = self.driver.title
        assert title == "avianca - encuentra tiquetes y vuelos baratos | Web oficial", f"Título incorrecto: se obtuvo '{title}'"

    #Validar el idioma
    def validar_idioma(self):
        idioma =  self.driver.find_element(By.XPATH, "//div[@class='main-header_nav-secondary']//button[@class='dropdown_trigger dropdown_trigger--active']")
        idioma.click()

        lista_idiomas = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='dropdown_content ng-star-inserted']//ul//li"))
        )
        lista_idiomas[3].click()
        assert len(lista_idiomas) == 4, f"Se esperaban 4 idiomas, pero se encontraron {len(lista_idiomas)}"
    
    #Validar paises
    def validar_pais(self):
        pais =  self.driver.find_element(By.XPATH, "//div[@class='main-header_nav-secondary']//button[@id='pointOfSaleSelectorId']")
        pais.click()
        boton_cerrar = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='points-of-sale_header_close-button']"))
        )
        lista_paises = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='pointOfSaleListId']//li"))
        )
        assert len(lista_paises) == 22, f"Se esperaban 22 paises, pero se encontraron {len(lista_paises)}"
        boton_cerrar.click()
        
    #Se encarga de configurar el vuelo para solo ida
    def seleccionar_solo_ida(self):
        solo_ida = self.driver.find_element(By.ID, "journeytypeId_1")
        solo_ida.click()
    
    #Selecciona el origen de partida
    def seleccionar_origen(self, origen):
        origen_padre = self.driver.find_element(By.ID, "originDiv")
        input_origen = origen_padre.find_element(by=By.CLASS_NAME, value="control_field_input")
        origen_padre.click()
        input_origen.send_keys(origen)

        select_origen = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='station-control-list_item_link']"))
        )
        select_origen.click()

    #Selecciona el destino de llegada
    def seleccionar_destino(self):
        lista_destino = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='arrivalStationsListId']//li"))
        )
        actions = ActionChains(self.driver)
        actions.click(lista_destino[1]).perform()

    #Se encarga de seleccionar los pasajeros(2 pasajeros)
    def seleccionar_pasajeros(self):
        boton_pasajeros = self.driver.find_element(By.XPATH, "//div[@class='ibe-search_pax-control']//button[@class='control_field_button']")
        boton_pasajeros.click()

        lista_pasajeros = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='pax-control_selector']//li"))
        )
        agregar_pasajero_adulto = lista_pasajeros[1].find_element(By.XPATH, ".//button[@class='ui-num-ud_button plus']")
        agregar_pasajero_adulto.click()
    
    #Confirma los pasajeros seleccionados
    def confirmar_pasajeros(self):
        boton_de_confirmacion = self.driver.find_element(By.XPATH, "//button[@class='button control_options_selector_action_button']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", boton_de_confirmacion)
        time.sleep(1)
        boton_de_confirmacion.click()

    #Realiza la busqueda de los vuelos disponibles
    def buscar(self):
        boton_de_buscar = self.driver.find_element(by=By.ID, value="searchButton")
        boton_de_buscar.click()

    #Configura el plan basico
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

    #Valida que el sumary quedo con el plan basico seleccionado
    def validar_summary(self):
        nombre_plan = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "journey_price_fare_name-text"))
        )

        contenedor = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "journey_price")))
        assert "basic" in contenedor.text.lower(), "El texto 'basic' no se encuentra dentro del contenedor"

    #Despues de tener el vuelo configurado, esta funcion se encarga de dar cleck en continuar
    def continuar(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))

        boton_continuar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button page_button btn-action page_button-primary-flow ng-star-inserted']"))
        )
        boton_continuar.click()

    #Esta funcion actualiza los elementos encontrados para ese XPATH cuando el DOM se actualiza
    def reasignar_botones(self):
        botones_pasajeros = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='passenger_data_group_item ng-star-inserted']//div[@class='ui-dropdown ng-star-inserted']//button"))
        )
        return botones_pasajeros
    
    #Las siguientes funciones, generan nombre, apellido, telefono y correo aleatoriamente
    #utilizando la libreria faker
    def generar_nombre(self):
        return fake.first_name()
    
    def generar_apellido(self):
        return fake.last_name()

    def generar_telefono(self):
        return str(random.randint(10_000_000, 99_999_999))
    
    def generar_correo(self):
        nombre = fake.first_name().lower()
        apellido = fake.last_name().lower()
        numero = random.randint(1, 999)
        dominio = random.choice(["gmail.com"])
        return f"{nombre}.{apellido}{numero}@{dominio}"
    
    #Las siguientes funciones, llenan los campos de los pasajeros, el genero, nombre, apellido,
    #fecha de nacimiento y la nacionalidad.
    def llenar_el_campo_genero(self, posicion_boton, posicio_opcion):
        botones = self.reasignar_botones()
        botones[posicion_boton].click()
        botones = self.reasignar_botones()
        botones[posicio_opcion].click()
    
    def llenar_los_campos_nombres_y_apellidos(self, posicion_nombre, posicion_apellido):
        campos_de_texto = self.driver.find_elements(By.XPATH, "//div[@class='passenger_data_group_item ng-star-inserted']//ibe-input//input")
        nombre = self.generar_nombre()
        campos_de_texto[posicion_nombre].send_keys(nombre)
        apellido = self.generar_apellido()
        campos_de_texto[posicion_apellido].send_keys(apellido)

    def llenar_el_campo_fecha_de_nacimiento(
        self, posicion_opcion1, posicion_opcion2, posicion_opcion3, posicion_opcion4, posicion_opcion5, posicion_opcion6
        ):
        botones = self.reasignar_botones()
        botones[posicion_opcion1].click()
        botones = self.reasignar_botones()
        botones[posicion_opcion2].click()
        botones = self.reasignar_botones()
        botones[posicion_opcion3].click()
        botones = self.reasignar_botones()
        botones[posicion_opcion4].click()
        botones = self.reasignar_botones()
        botones[posicion_opcion5].click()
        botones = self.reasignar_botones()
        botones[posicion_opcion6].click()

    def llenar_el_campo_nacionalidad(
        self, posicion_opcion1, posicion_opcion2
        ):
        botones = self.reasignar_botones()
        botones[posicion_opcion1].click()
        botones = self.reasignar_botones()
        botones[posicion_opcion2].click()

    #Se encarga de llenar los datos del titular de la reserva, los acepta y continua
    def llenas_campos_del_titular(self):
        botones_titular = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='contact_data']//button"))
        )
        botones_titular[0].click()
        botones_titular = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='contact_data']//button"))
        )
        botones_titular[1].click()
        inputs_titular = self.driver.find_elements(By.XPATH, "//div[@class='contact_data']//input")
        inputs_titular[0].send_keys(self.generar_telefono())
        inputs_titular[1].send_keys(self.generar_correo())

    def aceptar_y_continuar(self):
        aceptar_uso_de_datos_personales = self.driver.find_element(by=By.ID, value="sendNewsLetter")
        aceptar_uso_de_datos_personales.click()
        self.continuar()
        