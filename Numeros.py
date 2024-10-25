#Autores: Alejandro Inzulza y Eduardo Olguin
def abrir_archivo(nombre_archivo):
    salida = []
    archivo = open(nombre_archivo, "r")   
    contenido = archivo.readlines()
    for lineas in contenido:
        salida.append(lineas.strip().split())
    archivo.close()
    return salida
        
def identificar_numeros(palabras, numeros_palabras, escalas_palabras):
    numeros_digitados = []
    
    for numeros in palabras:
        suma_temporal = 0
        es_negativo = False

        for num in numeros:
            if num in numeros_palabras:
                suma_temporal += numeros_palabras[num]
            elif num in escalas_palabras:
                suma_temporal *= escalas_palabras[num]
            elif num == "negative":
                es_negativo = True
        
        if es_negativo == True:
            suma_temporal *= -1
        
        numeros_digitados.append(suma_temporal)
    
    return numeros_digitados           

def generar_salida(nombre_salida, numeros):
    archivo = open(nombre_salida, "w")
    for num in numeros:
        archivo.write(str(num) + "\n")
    archivo.close()                            

if __name__=="__main__":
    nombre_archivo = "en_palabras.txt"
    nombre_salida = "en_numeros.txt"
    numeros_palabras = {"zero": 0, "one":1, "two":2, "three": 3, "four": 4, "five": 5,
                        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
                        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                        "seventeen": 17, "eighteen": 18, "nineteen": 19,"twenty": 20, "thirty": 30,
                        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90 }
    escalas_palabras = {"hundred": 100, "thousand": 1000, "million": 1000000}
    palabras = abrir_archivo(nombre_archivo)
    numeros = identificar_numeros(palabras, numeros_palabras, escalas_palabras)
    generar_salida(nombre_salida, numeros)
    