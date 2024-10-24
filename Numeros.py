#Autores: Alejandro Inzulza y Eduardo Olguin
def abrir_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")                           
    contenido = archivo.read().split("\n")
    archivo.close()
    return contenido
         
def identificar_numeros(palabras, numeros_palabras, escalas_palabras):
    numeros_digitados = []
    total = 0
    suma_temporal = 0
            

def generar_salida():
    pass
                
            




if __name__=="__main__":
    nombre_archivo = "en_palabras.txt"
    numeros_palabras = {"zero": 0, "one":1, "two":2, "three": 3, "four": 4, "five": 5,
                        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
                        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                        "seventeen": 17, "eighteen": 18, "nineteen": 19,"twenty": 20, "thirty": 30,
                        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90 }
    escalas_palabras = {"hundred": 100, "thousand": 1000, "million": 1000000}
    palabras = abrir_archivo(nombre_archivo)
    numeros = identificar_numeros(palabras, numeros_palabras, escalas_palabras)
    