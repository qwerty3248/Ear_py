
from gtts import gtts
import os
from googletrans import Translator

rumano = 'ro'
espanol = 'es'
ingles = 'en'
frances = 'fr'
italiano = 'it'
japones = 'ja'

def Traduccion(texto,destino):
    translator = Translator()
    traduccion = translator.translate(texto,dest = destino)
    return traduccion.text



def main ():
    idioma = input("Introduzca uno [rumano] [japones] [ingles] [italiano] [frances] ")
    while idioma != rumano && idioma != japones && idioma != ingles && idioma != italiano && idioma != frances:
        idioma = input("Introduzca un idioma valido [rumano] [japones] [ingles] [italiano] [frances] ")

    oraciones = []

    while True:
        oracion = input("Introduce una oración (o escribe 'salir' para terminar): ")

        if oracion.lower() == 'salir':
            break
        
            

        oraciones.append(oracion)

        if len(oraciones) >= 3:
            break

    



if __name__ == "__main__":
    main()    



