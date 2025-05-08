#Importaciones necesarias, pytest para ejecutar el test, selenium y el page donde esta
#la logica del test y los localizadores
import pytest
from selenium import webdriver
from src.pages.caso1_page import Caso1Page
import allure

#Configurado para que funcione con pytest, que funcione con el navegador Chrome
#y agrande la pantalla para una mejor ejecucion cuando tiene que hacer scroll.
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Reserva de vuelos")
@allure.story("Reserva solo ida para dos pasajeros")
@allure.title("Reserva solo ida con pasajeros y datos completos")
def test_reserva_solo_ida(setup):
    driver = setup
    pagina = Caso1Page(driver)

    with allure.step("Reserva solo ida"):
        #Llama la funcion cargar y es la que se encarga de abrir la pagina
        pagina.cargar("https://nuxqa4.avtest.ink/")
        pagina.tomar_captura(driver, "pantalla_inicio")

        #Validar idiomas
        pagina.validar_idioma()

        
        #Selecciona la configuracion de solo ida
        pagina.seleccionar_solo_ida()

        #Selecciona el origen de salida
        pagina.seleccionar_origen("Medellin")

        #Selecciona el destino
        pagina.seleccionar_destino()

        #Selecciona Los pasajeros y los confirma
        pagina.seleccionar_pasajeros()
        pagina.confirmar_pasajeros()
        pagina.tomar_captura(driver, "Pantalla de seleccion de pasajeros")
        pagina.buscar()

        #Selecciona el plan y valida que si quede selccionado en el sumary
        pagina.seleccionar_plan()
        pagina.validar_summary()
        pagina.continuar()

        #Llenar campos del pasajero 1
        pagina.llenar_el_campo_genero(0, 1)
        pagina.llenar_los_campos_nombres_y_apellidos(0, 1)
        pagina.llenar_el_campo_fecha_de_nacimiento(1, 2, 2, 4, 3, 5)
        pagina.llenar_el_campo_nacionalidad(4, 5)
        pagina.tomar_captura(driver, "Campos del pasajero 1")

        #Llenar campos del pasajero 2
        pagina.llenar_el_campo_genero(6, 7)
        pagina.llenar_los_campos_nombres_y_apellidos(2, 3)
        pagina.llenar_el_campo_fecha_de_nacimiento(7, 9, 8, 10, 9, 12)
        pagina.llenar_el_campo_nacionalidad(10, 11)

        #Titular de la reserva
        pagina.llenas_campos_del_titular()

        #Aceptar el uso de datos personales
        pagina.aceptar_y_continuar()
