<<<<<<< HEAD
import cv2
import requests
import numpy as np
from io import BytesIO

# URL de la imagen que quieres cargar
url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'

# Descargar la imagen desde la URL
respuesta = requests.get(url)
imagen_bytes = BytesIO(respuesta.content)
imagen_array = np.asarray(bytearray(imagen_bytes.read()), dtype=np.uint8)

# Decodificar la imagen usando OpenCV
imagen = cv2.imdecode(imagen_array, cv2.IMREAD_COLOR)

# Verificar si la imagen se cargó correctamente
if imagen is not None:
    # Obtener el tamaño de la imagen (altura y ancho)
    alto, ancho = imagen.shape[:2]
    ratio =  radio(ancho, alto)
    print(f'Tamaño de la imagen: {ancho}x{alto} y ratio: {ratio}')
    
else:   
    print('No se pudo cargar la imagen desde la URL proporcionada.')


def radio(ancho, alto):
    aspect_radio = ancho/alto
    if aspect_radio == 4/3:
        var = "Aspect radio 4:3"
        return var
    elif aspect_radio == 16 / 9:
        var = "Aspect radio 16:9"
        return var
    elif aspect_radio == 1:
        var = "Aspect radio 1:1 (Cuadrada)"
        return var
    elif aspect_radio == 21 / 9:
        var = "Aspect radio = 21:9"
        return var
    else:
        var = "Otro ratio"
        return var
=======
import cv2
import requests
import numpy as np
from io import BytesIO

# URL de la imagen que quieres cargar
url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'

# Descargar la imagen desde la URL
respuesta = requests.get(url)
imagen_bytes = BytesIO(respuesta.content)
imagen_array = np.asarray(bytearray(imagen_bytes.read()), dtype=np.uint8)

# Decodificar la imagen usando OpenCV
imagen = cv2.imdecode(imagen_array, cv2.IMREAD_COLOR)

# Verificar si la imagen se cargó correctamente
if imagen is not None:
    # Obtener el tamaño de la imagen (altura y ancho)
    alto, ancho = imagen.shape[:2]
    ratio =  radio(ancho, alto)
    print(f'Tamaño de la imagen: {ancho}x{alto} y ratio: {ratio}')
    
else:   
    print('No se pudo cargar la imagen desde la URL proporcionada.')


def radio(ancho, alto):
    aspect_radio = ancho/alto
    if aspect_radio == 4/3:
        var = "Aspect radio 4:3"
        return var
    elif aspect_radio == 16 / 9:
        var = "Aspect radio 16:9"
        return var
    elif aspect_radio == 1:
        var = "Aspect radio 1:1 (Cuadrada)"
        return var
    elif aspect_radio == 21 / 9:
        var = "Aspect radio = 21:9"
        return var
    else:
        var = "Otro ratio"
        return var
>>>>>>> cca8414323dade681936e1d599d1daac71b40e7a
    