import sys

# from utils.peticiones import (
#     solicitar_token, 
#     solicitar_lista_imagenes,
#     descargar_imagen)
from utils.peticiones import *
from utils.utilitarios import inicializar_carpetas
from utils.imagenes import modificar_imagenes

def main():
    
    # Solicitamos los datos al usaurio
    cantidad_imagenes = input("Digite la cantidad de imágenes que desea descargar: ")
    cantidad_imagenes = int(cantidad_imagenes)

    # Solicitamos el token
    token = solicitar_token()
    if token == None:
        # Si no hay token, mostramos un mensaje de error y salimos
        print("El token no se ha podido generar. Vuelva a correr el programa.")
        sys.exit("Fin del programa!")

    # Descargamos las imágnes
    lista_imagenes = solicitar_lista_imagenes(token, cantidad_imagenes)
    if lista_imagenes == None:
        # Si no hay imágenes, mostrarmos un mensaje de error y salimos
        print("No se ha podido recuperar el listado de las imágenes. Vuelva a correr el programa.")
        sys.exit("Fin del programa!")

    # Descargamos una a una las imágenes de la lista, mediante la url
    for index, url in enumerate(lista_imagenes):        
        print("Descargando imagen", index + 1, "de", len(lista_imagenes))
        descargar_imagen(url)

    # Mandamos a modificar las imágenes
    modificar_imagenes()

if __name__ == "__main__":
    inicializar_carpetas()
    main()