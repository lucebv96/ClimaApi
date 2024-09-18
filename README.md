# Aplicación CLI para Consultar el Pronóstico del Clima

Este proyecto es una aplicación de línea de comandos (CLI) que permite consultar el pronóstico del clima para cualquier ciudad, utilizando la API de OpenWeather. La aplicación te permite obtener los datos en formato de texto o JSON.

## Características

- Consulta el pronóstico del clima para cualquier ciudad del mundo.
- Muestra la temperatura actual, la sensación térmica, la humedad, la visibilidad y el pronóstico general.
- Opción de salida en formato `json` o `text`.
- Interfaz de línea de comandos sencilla y fácil de usar.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/lucebv96/ClimaApi.git
    cd ClimaApi
    ```

2. Instala las dependencias necesarias con pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Crea un archivo `apikey.py` en la raíz del proyecto y agrega tu clave de API de OpenWeather:

    ```python
    API_KEY = 'tu_clave_de_api_aqui'
    ```

## Uso

Para utilizar la aplicación, debes especificar el nombre de la ciudad y puedes elegir el formato de salida (texto o JSON).

### Ejemplo de uso:

```bash
python main.py Madrid --output json```
