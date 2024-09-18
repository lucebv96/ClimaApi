import click
import requests
import json
from apikey import API_KEY


# Función para convertir Kelvin a Celsius
def tranf_celsius(kelvin):
    return kelvin - 273.15

# Función principal que obtiene y muestra la información climática
@click.command(help="Aplicación CLI para consultar el pronóstico del clima usando la API de OpenWeather.")
@click.argument('ciudad')
@click.option('--output', type=click.Choice(['json','text'], case_sensitive=False), default='text', help='Formato de salida: json o txt')
def mostrar_clima(ciudad, output):
    """Consulta y muestra el pronóstico del clima para la CIUDAD especificada."""
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    
    url = BASE_URL + "appid=" + API_KEY + '&q=' + ciudad + '&lang=es'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hay errores en la solicitud

        data = response.json()

        # Verificar si la ciudad fue encontrada
        if data.get('cod') == '404':
            click.echo(f"Error: No se encontró la ciudad '{ciudad}'. Por favor, verifica el nombre e intenta nuevamente.")
            return

        # Extraer datos
        temp_kelvin = data['main']['temp']
        temp_celsius = tranf_celsius(temp_kelvin)
        sens_termica_kelvin = data['main']['feels_like']
        sens_termica_celsius = tranf_celsius(sens_termica_kelvin)
        pronostico = data['weather'][0]['description']
        humedad = data['main']['humidity']
        visibilidad = data['visibility']

        # Formatear la salida según el tipo especificado
        if output == 'json':
            clima_info = {
                'ciudad': ciudad,
                'temperatura_celsius':f'{temp_celsius:.2f}°C',
                'sensacion_termica_celsius': f'{sens_termica_celsius:.2f}°C',
                'pronostico': pronostico,
                'humedad': f'{humedad}%',
                'visibilidad_m': f'{visibilidad} mts' 
            }
            click.echo(json.dumps(clima_info, indent=4, ensure_ascii=False))
        
        
        else:  # output == 'text'
            click.echo(f"A continuación el pronóstico en {ciudad}:\n")
            click.echo(f"Temperatura actual: {temp_celsius:.2f}°C")
            click.echo(f"Sensación térmica: {sens_termica_celsius:.2f}°C")
            click.echo(f"Pronóstico: {pronostico}")
            click.echo(f"Humedad: {humedad}%")
            click.echo(f"Visibilidad: {visibilidad} m")

    except requests.exceptions.HTTPError:
        click.echo(f"Error: No se encontró la ciudad '{ciudad}'. Por favor, verifica el nombre e intenta nuevamente.")
    except requests.exceptions.RequestException as err:
        click.echo(f"Error de conexión: {err}")

if __name__ == '__main__':
    mostrar_clima()
