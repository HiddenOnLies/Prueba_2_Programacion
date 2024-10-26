# Autores: Alejandro Inzulza y Eduardo Olguin


# Función para abrir el archivo y almacenar su contenido en una lista.
def abrir_archivo(nombre_entrada):
    salida = [] 
    archivo = open(nombre_entrada, "r") 
    contenido = archivo.readlines()  
    for lineas in contenido:  
        palabras = lineas.strip("").split() 
        if len(palabras) >= 1:  # Condición que solamente almacena las lineas que contengan una o mas palabras.
            salida.append(palabras) 
    archivo.close()  
    return salida 


# Función que almacena los diccionarios de numeros y escalas y los retorna a dos variables. 
def variables_numeros():
    numeros = {"zero": 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
                "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, "eleven" : 11,
                "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16,
                "seventeen" : 17, "eighteen" : 18, "nineteen" : 19,"twenty" : 20, "thirty" : 30,
                "forty" : 40, "fifty" : 50, "sixty" : 60, "seventy" : 70, "eighty" : 80, "ninety" : 90}
    escalas = {"hundred" : 100, "thousand" : 1000, "million" : 1000000, "millions" : 1000000}  # Almacenamos million y millions para evitar posibles errores.
    return numeros, escalas
        

# Función que convierte los elementos de una lista de palabras a su equivalente numérico del diccionario.
def identificar_numeros(palabras, numeros_palabras, escalas_palabras):
    numeros_digitados = []  
    for numeros in palabras:
        total = 0  
        suma_temporal = 0  
        es_negativo = False  
        for num in numeros:
            if num in numeros_palabras:  
                suma_temporal += numeros_palabras[num]  # Suma valores contenidos en el diccionario "numeros".
            elif num in escalas_palabras: 
                if num == "hundred":  
                    suma_temporal *= escalas_palabras[num]  # Multiplica por la escala de cien.
                else:  
                    total += suma_temporal * escalas_palabras[num]  # Multiplica por escalas de mil o millon.
                    suma_temporal = 0  # Reiniciamos la variable para evitar errores de calculo entre las escalas de mil y millón.
            elif num == "negative":  
                es_negativo = True  # Marca en caso de que nos indique que el número sera negativo.
        total += suma_temporal  
        if es_negativo == True: 
            total *= -1  # Transformamos el número a negativo en caso de que se cumpla la condición.
        numeros_digitados.append(total)  
    return numeros_digitados  


# Función para generar un archivo de salida con la lista que contiene los números convertidos a enteros.
def generar_salida(nombre_salida, numeros):
    archivo = open(nombre_salida, "w")  
    for num in numeros:
        archivo.write(str(num) + "\n") # Escribimos cada número en una nueva línea.
    archivo.close()           


if __name__ == "__main__":
    # Nombres de los archivos de entrada y salida.
    nombre_entrada = "en_palabras.txt"
    nombre_salida = "en_numeros.txt"
    # Obtenemos los diccionarios de números y escalas.
    numeros_palabras, escalas_palabras = variables_numeros()
    # Procesamos el archivo de entrada y convertimos las palabras a números.
    palabras = abrir_archivo(nombre_entrada)
    numeros = identificar_numeros(palabras, numeros_palabras, escalas_palabras)
    # Generamos el archivo de salida con los números convertidos.
    generar_salida(nombre_salida, numeros) 
    