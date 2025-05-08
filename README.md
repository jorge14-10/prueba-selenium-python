# prueba-selenium-python

Este proyecto describe los pasos necesarios para instalar las dependencias requeridas y configurar el entorno para ejecutar las pruebas automatizadas de Selenium con pytest.

## Requisitos Previos

1. Tener **Python** instalado (versión 3.8 o superior).
2. Tener **pip** (gestor de paquetes de Python) instalado.
3. Instalar **Selenium** para la automatización de pruebas web.
4. Instalar **pytest** para la ejecución y gestión de las pruebas.
5. Descargar el **WebDriver** adecuado, dependiendo del navegador que uses, como **ChromeDriver** o **GeckoDriver**.

## Instalación de Dependencias

1. Si no tienes **Python** instalado, puedes descargarlo desde el [sitio oficial de Python](https://www.python.org/downloads/) según el sistema operativo que estés utilizando.

2. Crear un entorno virtual con el siguiente comando:

   ```bash
   python -m venv venv

3. Activar entorno virtual:

   En windows:
    ```bash
    .\venv\Scripts\activate

   En macOS/Linux:
    ```bash
    source venv/bin/activate

4. Instalar las dependencias desde el archivo requirements.txt:

    ```bash
    pip install -r requirements.txt

5. Ejecucion de pruebas:

    pytest [ruta_del_test]

    ejemplo:
    ```bash
   pytest src/tests/caso1_reserva_one_way.py


## Pasos adicionales para poder visualizar el reporte de ejecución en Allure

### 1. Instalación de Allure

#### Para macOS (usando Homebrew):

```bash
brew install allure
```

#### Para Linux (usando wget):

```bash
wget https://github.com/allure-framework/allure2/releases/download/2.17.3/allure-2.17.3.zip
unzip allure-2.17.3.zip
sudo mv allure-2.17.3 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/local/bin/allure
```

#### Para Windows:

1. Ve a la [página de releases de Allure](https://github.com/allure-framework/allure2/releases).
2. Descarga el archivo `.zip` más reciente.
3. Extrae el archivo descargado.
4. Agrega la ruta donde extrajiste Allure a la variable de entorno `PATH`. Esto permitirá ejecutar el comando `allure` desde cualquier lugar en la terminal.

#### Verificar la instalación:

```bash
allure --version
```

### 2. Visualizar el reporte de ejecución en Allure

Luego de ejecutar tus pruebas con `pytest` y haber generado los resultados, usa el siguiente comando para ver el reporte en el navegador:

```bash
allure serve report/
```

