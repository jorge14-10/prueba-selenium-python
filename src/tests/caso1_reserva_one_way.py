# src/tests/caso1_reserva_one_way.py

import pytest
from selenium import webdriver
from src.pages.caso1_page import Caso1Page

from faker import Faker
import random

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_reserva_solo_ida(setup):
    driver = setup
    pagina = Caso1Page(driver)
    pagina.cargar("https://nuxqa4.avtest.ink/")
    pagina.seleccionar_solo_ida()
    pagina.seleccionar_origen("Medellin")
    pagina.seleccionar_destino()
    pagina.seleccionar_pasajeros()
    pagina.confirmar_pasajeros()
    pagina.buscar()
    pagina.seleccionar_plan()
    pagina.validar_summary()
    pagina.continuar()

    #llenar los campo de pasajeros

