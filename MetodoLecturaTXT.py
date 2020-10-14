#se define la funcion que desarrollara el proceso de analizar el texto
def analizar_texto(path_archivo_entrada: str, path_archivo_salida: str) -> int:
    #se crea una variable que abre el archivo de lectura
    archivo_entrada = open(path_archivo_entrada, 'r')
    #se le dice que lea dicho archivo
    linea_texto = archivo_entrada.readline()
    #se cierra el archivo
    archivo_entrada.close()
    #se define que es lo que divide cada palabra en el texto de entrada
    linea_texto_separada = linea_texto.split("_")
    #se crea una variable que identifica palabras repetidas
    dicionaro_ocurrencias = {}
    #se crea una funcion recurrente que cuenta la cantidad de veces que aparece cada palabra
    for palabra in linea_texto_separada:
        ocurrencias = 0
        for otra_palabra in linea_texto_separada:
            if palabra == otra_palabra:
                ocurrencias += 1
        dicionaro_ocurrencias[palabra] = ocurrencias
    #se crea un archivo de escritura de salida
    archivo_salida = open(path_archivo_salida, 'w')
    #se agrega cada palabra con su numero de ocurrencias al documento de salida
    for ocurrencia in dicionaro_ocurrencias:
        archivo_salida.write(ocurrencia + " | " + str(dicionaro_ocurrencias[ocurrencia]) + "\n")
    archivo_salida.close()
    return 1


if __name__ == '__main__':
    analizar_texto("D:\\Users\\Alberto\\Documents\\testa.txt", "D:\\Users\\Alberto\\Documents\\salida.txt")
