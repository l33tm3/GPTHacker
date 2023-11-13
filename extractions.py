import requests
from bs4 import BeautifulSoup
import json

def extraer_texto(url):
    # Obtener el contenido de la página web
    try:
        respuesta = requests.get(url)
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        # Extraer el texto del cuerpo del sitio web
        texto = soup.get_text()

        # Limpieza básica del texto (puede ampliarse según necesidades)
        texto_limpio = texto.replace('\n', ' ').replace('\r', '').strip()

        return texto_limpio
    except Exception as e:
        print(f"Error al extraer el texto: {e}")
        return None

def guardar_como_json(texto, nombre_archivo):
    # Estructura de datos en formato JSON
    datos = {
        "texto": texto
    }

    # Guardar datos en un archivo JSON
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

# Solicitar al usuario que ingrese la URL
url = input("Ingresa la URL del sitio web: ")

# Ejecutar la extracción y guardado si la URL es válida
texto = extraer_texto(url)
if texto:
    guardar_como_json(texto, 'texto_web.json')