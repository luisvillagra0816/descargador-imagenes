import os
import shutil

def inicializar_carpetas():
    ruta = "imagenes_descargadas"
    shutil.rmtree(ruta)
    os.makedirs(ruta)