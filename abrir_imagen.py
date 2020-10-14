# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 02:03:04 2020

@author: Esteban Salazar C
"""

from PIL import Image # Librería necesaria
#   import time # para contador de tiempo
### parámetros de entrada arir imagen:
### im: nombre de la imagen sin extensión
### input_ruta: se coloca la direccion del archivo
### scale: 0 para 1:1, 1 para 1:2, 2 para 2:1
def abrir_imagen(im,input_rute,scale): # función
#   tiempoIn = time.time() # inicia conteo de tiempo
    im = im + '.jpg' # solo permite extensión jpg
    # a continuación se establece la ruta para la dirección de la img.jpg:
    ruta = (input_rute + im) 
    im = Image.open(ruta) # función de Image para abrir la ruta de la imagen
    ancho = im.width # ancho de la imagen
    alto = im.height # alto de la imagen 
    xcuadro = int((ancho + alto)/2) # variable que crea una arista de cuadro 
    if scale == 0: # Escala 1:1
        new_scale = im.resize((xcuadro,xcuadro))
#       print(new_scale.size)
        new_scale.show() # muestra la imagen
        return 0
    if scale == 1: # Escala 1:2
        new_scale = im.resize((xcuadro,xcuadro*2))
#       print(new_scale.size)
        new_scale.show() # muestra la imagen
        return 1
    if scale == 2: # Escala 2:1
        new_scale = im.resize((xcuadro*2,xcuadro))
#       print(new_scale.size)
        new_scale.show() # muestra la imagen
        return 2
    else:
        return 532
#  tiempoFin = time.time() # finaliza conteo de tiempo
#  print('El Proceso Tardó: ', tiempoFin - tiempoIn, 'Segundos') # print time