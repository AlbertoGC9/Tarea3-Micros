# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import time 

def abrir_imagen(im):
    tiempoIn = time.time()
    ruta = (r"C:\Users\Admin\Documents\2020\II\Sensores\PC2" + im)
    im = Image.open(ruta)
    im.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')
          