import click
import requests 
from apikey import API_KEY
#Funcion para convertir Kelvin a Celsius

def tranf_celsius(kelvin):
    return kelvin-273.15


@click.command()
@click.argument('ciudad')
#funcion principal que obtienen y muestra la info climatica
def mostrar_clima(ciudad):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    
    url = BASE_URL + "appid=" + API_KEY + '&q=' + ciudad + '&lang=es'


    response = requests.get(url).json()
    #print(response)

    temp_kelvin = response['main']['temp']
    temp_celsius = tranf_celsius(temp_kelvin)
    
    print(f'La temperatura en {ciudad} es  {temp_celsius:.2F}°C')
    


mostrar_clima()