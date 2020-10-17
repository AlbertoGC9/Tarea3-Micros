from pygame import mixer #Importa la librería

mixer.init() #Inicial el método
mixer.music.load('d:/Users/Alberto/Documents/TEC/Semestre II - 2020/Microprocesadores y Microcontroladores/Tarea 3/piano.mp3') #Carga el documento .mp3
mixer.music.play(5) #Determina la cantidad de veces que corre el .mp3, en este caso, 5 veces
