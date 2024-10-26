# Autores: Alejandro Inzulza y Eduardo Olguin


# Funcion para abrir el archivo y almacenar su contenido en una lista.
def abrir_archivo(nombre_archivo):
    salida = []  # Lista vacia que almacenara las lineas en listas y las palabras en sublistas.
    archivo = open(nombre_archivo, "r")  # Abrir el archivo en en modo lectura.
    contenido = archivo.readlines()  # Leemos todas las lineas del archivo y las almacenamos en una variable.
    for lineas in contenido:  # Recorrer cada linea del archivo.
        palabras = lineas.strip("").split()  # Eliminamos espacios en blanco al inicio y final de las palabras y separamos cada palabra.
        if len(palabras) >= 1:  # Condicion para solamente almacenar las lineas que contengan una o mas palabras.
            salida.append(palabras)  # Agregamos las palabras que cumplen con esta condicion a la lista.
    archivo.close()  # Cerrar el archivo.
    return salida  # Retornamos la lista que almacena las palabras.


# Funcion que almacena los diccionarios y los retorna a dos variables. 
def variables_numeros():
    # Diccionario que relaciona las palabras a numeros enteros.
    numeros = {"zero": 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
                "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, "eleven" : 11,
                "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16,
                "seventeen" : 17, "eighteen" : 18, "nineteen" : 19,"twenty" : 20, "thirty" : 30,
                "forty" : 40, "fifty" : 50, "sixty" : 60, "seventy" : 70, "eighty" : 80, "ninety" : 90}
    # Diccionario que relaciona palabras como escalas para facilitar la transformacion de palabras a numeros enteros.
    escalas = {"hundred" : 100, "thousand" : 1000, "million" : 1000000, "millions" : 1000000}  # Almacenamos million y millions para evitar posibles errores.
    return numeros, escalas # Retornamos ambas bibliotecas y las asociamos a dos variables.
        

# Funcion que convierte los elementos de una lista de palabras a su equivalente numerico.
def identificar_numeros(palabras, numeros_palabras, escalas_palabras):
    numeros_digitados = []  # Lista vacia que almacenara los numeros transformados a enteros.
    for numeros in palabras:  # Recorremos los elementos de la lista. 
        total = 0  # Variable que almacenara el resultado final al transformar el numero.
        suma_temporal = 0  # Variable que acumula temporalmente la suma antes de aplicar una escala.
        es_negativo = False  # Variable booleana que si es verdadera transforma el numero entero a negativo.
        for num in numeros:  # Recorremos cada elemento de la sublista.
            if num in numeros_palabras:  # Condicion si la palabra esta dentro del diccionario de numeros.
                suma_temporal += numeros_palabras[num]  # Se sumara su valor como numero entero a la variable "suma_temporal".
            elif num in escalas_palabras:  # Condicion si la palabra esta dentro del diccionario de escalas.
                if num == "hundred":  # Condicion si la palabra es "hundred".
                    suma_temporal *= escalas_palabras[num]  # la suma temporal se multiplicara por cien.
                else:  # Si la condicion anterior no se cumple.
                    total += suma_temporal * escalas_palabras[num]  # Se multiplicara la suma temporal por las escalas de miles o de millon y se almacenara en la variable "total".
                    suma_temporal = 0  # La suma temporal volvera a ser 0 para evitar errores de calculo entre la escala de cien y el resto de escalas.
            elif num == "negative":  # Condicion si la palabra es "negative".
                es_negativo = True  # La variable booleana "es_negativo" sera verdadera.
        total += suma_temporal  # A la variable "total" se le sumara la variable "suma_temporal".
        if es_negativo == True: # Si la variable booleana "es_negativo" es verdadera.
            total *= -1  # La variable total sera multiplicada por -1 para transformar el numero a negativo.
        numeros_digitados.append(total)  # El resultado de la variable "total" sera almacenado en la lista.
    return numeros_digitados  # Retornamos la lista con los numeros que fueron transformados.


# Función para generar un archivo de salida con los números convertidos.
def generar_salida(nombre_salida, numeros):
    archivo = open(nombre_salida, "w")  # Abrimos el archivo en modo escritura.
    for num in numeros:  # Recorremos cada elemento de la lista y lo escribimos en el archivo de salida.
        archivo.write(str(num) + "\n")
    archivo.close()  # Cerramos el archivo.                   


if __name__ == "__main__":
    nombre_archivo = "en_palabras.txt"  # Nombre del archivo de entrada con numeros en palabras.
    nombre_salida = "en_numeros.txt"  # Nombre del archivo de salida con los numeros convertidos. 
    numeros_palabras, escalas_palabras = variables_numeros() # Obtener los diccionarios que almacenan numeros y escalas.
    palabras = abrir_archivo(nombre_archivo)  # Abrimos y procesamos el archivo de entrada.
    numeros = identificar_numeros(palabras, numeros_palabras, escalas_palabras)  # Identificamos y convertimos los numeros expresados en palabras a enteros.
    generar_salida(nombre_salida, numeros)  # Generamos el archivo de salida con los numeros convertidos a enteros.
    