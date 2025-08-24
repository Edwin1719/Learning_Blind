
import requests
from bs4 import BeautifulSoup
import sys

def crear_lista_palabras():
    """
    Descarga la lista de frecuencia de palabras en español desde Wiktionary
    y la guarda en un archivo palabras.txt.
    """
    url = "https://en.wiktionary.org/wiki/User:Matthias_Buchmeier/Spanish_frequency_list-1-5000"
    
    print(f"Descargando la lista de palabras desde {url}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la petición falla
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la página: {e}")
        sys.exit(1)
        
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar el div principal que contiene el contenido de la página
    content_div = soup.find('div', class_='mw-parser-output')
    
    if not content_div:
        print("No se pudo encontrar el contenedor de contenido principal en la página.")
        sys.exit(1)
        
    # El texto está dentro de párrafos <p> dentro de este div
    paragraphs = content_div.find_all('p')
    
    palabras = []
    for p in paragraphs:
        lines = p.get_text().strip().split('\n')
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 2 and parts[0].isdigit():
                # La palabra es el segundo elemento
                palabra = parts[1]
                palabras.append(palabra)

    if not palabras:
        print("No se pudieron extraer palabras. La estructura de la página puede haber cambiado.")
        sys.exit(1)

    try:
        with open('palabras.txt', 'w', encoding='utf-8') as f:
            for palabra in palabras:
                f.write(f"{palabra}\n")
    except IOError as e:
        print(f"Error al escribir en el archivo palabras.txt: {e}")
        sys.exit(1)

    print(f"¡Éxito! Se ha creado el archivo 'palabras.txt' con {len(palabras)} palabras.")

if __name__ == '__main__':
    crear_lista_palabras()
