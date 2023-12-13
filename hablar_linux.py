from gtts import gTTS
from googletrans import Translator
import pygame
import os
import time


rumano = 'ro'
espanol = 'es'
ingles = 'en'
frances = 'fr'
italiano = 'it'
japones = 'ja'
latin = 'la'
#chino = 'zh' no salen los caracteres chinos
indonesio = 'id'


def Traduccion(texto, destino):
    translator = Translator()
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text

def reproducir_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    print("Los idiomas en orden son rumano japones ingles italiano frances indonesio y latin en ese orden ")
    
    idioma = input("Introduzca uno [ro] [ja] [en] [it] [fr] [id] [la] ")
    
    while idioma not in [rumano, japones, ingles, italiano, frances, latin, indonesio]:
        idioma = input("Introduzca un idioma valido [ro] [ja] [en] [it] [fr] [id] [la] ")

    while True:
        oracion = input("Introduce una oración (o escribe 'salir' para terminar): ")

        if oracion.lower() == 'salir':
            break

        language = idioma  # No es necesario utilizar una variable adicional

        # Crear los objetos gTTS directamente
        tts_espanol = gTTS(text=oracion, lang=espanol)
        tts_idioma = gTTS(text=Traduccion(oracion, language), lang=language)

        # Guardar los archivos de audio como MP3
        tts_espanol.save("espanol.mp3")
        tts_idioma.save("idioma.mp3")

        # Imprimir la oración en español
        print(oracion)

        # Reproducir el archivo de audio en español con pygame
        reproducir_audio("espanol.mp3")

        #espera de 3 segundos 
        time.sleep(1)
	
        # Imprimir la traducción
        print(Traduccion(oracion, language))

        # Reproducir el archivo de audio de la traducción con pygame
        reproducir_audio("idioma.mp3")

        # Eliminar los archivos de audio después de reproducirlos
        os.remove("espanol.mp3")
        os.remove("idioma.mp3")

if __name__ == "__main__":
    main()

