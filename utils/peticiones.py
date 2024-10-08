import requests


def solicitar_token():

    """
    Solicita token JWT al servidor con las credenciales determinadas
    No recibe nada
    @returns: String con token o None si falla la conexión
    """

    # Definimos la url y los datos del cuerpo de la petición POST
    url = "https://python-course.lat/image-app/api-token-auth/"
    cuerpo = {
        "user": "user",
        "password": "python22024!"
    }

    # Relizamos la conexión al servidor
    response = None
    try:
        response = requests.post(url, data=cuerpo)
    except ConnectionError as e:
        print(e)
    
    # Si falla, devolvemos None
    if response == None:
        return None

    # Limpiamos el token y lo devolvemos
    token = response.text[1:-1]
    
    return token
    

def solicitar_lista_imagenes(token:str, cantidad_solicitada:int):
    
    url = "https://python-course.lat/image-app/images/"
    cuerpo = {
        "cantidad": cantidad_solicitada
    }
    encabezado = {
        "Authorization": f"Bearer {token}"
    }

    response=None
    try:
        response = requests.post(url, data=cuerpo, headers=encabezado)
    except ConnectionError as e:
        print(e)
    
    if response == None:
        return None
    
    return response.json()


def descargar_imagen(url:str):
    
    response = None
    try:
        response = requests.get(url)
    except ConnectionError as e:
        print(e)

    if response == None:
        print("No se ha podido obtener la imagen en la url", url)
        return
        
    nombre_archivo = url.split("/")[-1]

    ruta = f"imagenes_descargadas/{nombre_archivo}"

    with open(ruta, mode="wb") as archivo:
        archivo.write(response.content)
