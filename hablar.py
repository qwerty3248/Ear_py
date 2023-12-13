from gtts import gTTS
from googletrans import Translator
import os
import pygame
import time

# Lista de idiomas válidos
idiomas_validos = ['ro', 'ja', 'en', 'it', 'fr', 'id', 'la']

def Traduccion(texto, destino):
    translator = Translator()
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text

def reproducir_audio(file_path):
    # Inicializar el mezclador de Pygame y cargar el archivo de audio
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Esperar hasta que termine la reproducción
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Esperar un momento antes de continuar
    time.sleep(0.5)

    # Cerrar completamente el reproductor después de la reproducción
    pygame.mixer.quit()

def main():
    print("Los idiomas en orden son rumano, japonés, inglés, italiano, francés, indonesio y latín en ese orden")

    # Solicitar al usuario que ingrese un idioma válido
    idioma = input(f"Introduzca uno {idiomas_validos}: ").lower()

    # Validar la entrada del usuario
    while idioma not in idiomas_validos:
        idioma = input(f"Introduzca un idioma válido {idiomas_validos}: ").lower()

    while True:
        oracion = input("Introduce una oración (o escribe 'salir' para terminar): ")

        if oracion.lower() == 'salir':
            break

        language = idioma  # No es necesario utilizar una variable adicional

        try:
            # Crear los objetos gTTS directamente
            tts_espanol = gTTS(text=oracion, lang='es')
            tts_idioma = gTTS(text=Traduccion(oracion, language), lang=language)

            # Guardar los archivos de audio
            tts_espanol.save("espanol.mp3")
            tts_idioma.save("idioma.mp3")

            # Imprimir la oración en español y reproducir el audio
            print("Español:", oracion)
            reproducir_audio("espanol.mp3")

            # Pausa antes de continuar
            time.sleep(0.5)

            # Imprimir la traducción y reproducir el audio
            print(f"{idioma.capitalize()}: {Traduccion(oracion, language)}")
            reproducir_audio("idioma.mp3")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Eliminar los archivos de audio al final de cada iteración
            try:
                os.remove("espanol.mp3")
                os.remove("idioma.mp3")
            except FileNotFoundError:
                print("No se encontraron los archivos de audio para eliminar.")

if __name__ == "__main__":
    main()
