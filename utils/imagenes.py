import os

from PIL import Image, ImageFilter

def modificar_imagenes():

    # Establecemos la ruta en la que se encuentran las imágenes
    ruta_carpeta_imagenes = "imagenes_descargadas"

    # Obtenemos el listado de los nombres de las imágenes que se encuentran 
    # en la carpta
    nombres_imagenes = os.listdir(ruta_carpeta_imagenes)

    # Pasamos por cada imagen modificandolas
    for nombre_imagen in nombres_imagenes:

        # Establecemos la ruta de la imagen
        ruta_imagen = f"{ruta_carpeta_imagenes}/{nombre_imagen}"

        # Modificamos la imagen
        imagen = Image.open(ruta_imagen)

        imagen = imagen.convert("L") # B y N
        imagen = imagen.transpose(Image.FLIP_LEFT_RIGHT) # Transposición
        imagen = imagen.filter(ImageFilter.GaussianBlur(5)) # Difuminar
        imagen = imagen.rotate(-90) # Rotar en sentido horario

        # Establecemos la ruta en la que se guardará la imagen modificada
        ruta_nueva = f"{ruta_carpeta_imagenes}/modificada-{nombre_imagen}"
        imagen.save(ruta_nueva)
        imagen.close()
