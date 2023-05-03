'''
    La idea es intentar hacer un cifrado Hill más robusto que el original.
    
    Pasos: 
        - Necesitamos una frase para encriptar. Ejemplo: 'Este encriptado es muy robusto'
        - Dividiremos la frase en bloques de 3 hasta hacer una matriz de 3 x 3. Ejemplo: 'Est een cri pta doe smu yro bus to '
        - Cada letra la pasaremos a ascii
        - Crearemos una matriz clave de 3 x 3 de manera 'Aleatoria'
        - Multiplicaremos ambas matrices
        - El resultado sera una matrix de 3 x 3 la cual pasaremos a letras y recontruiremos los bloques de 3 letras
'''

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Importamos las librerias necesarias
import numpy as np
import random
from sympy import Matrix

# Variables globales
flag = True
message = ''
opcion = 0

# Con esta funcion pasamos una frase a matriz en ASCII
def matrizFrase(message):
    LISTA_TMP = []
    
    while len(message) % 3 != 0:        # Comprobamos que la longitud de la cadena sea multiplo de 3
        ascii = random.randrange(65,90) # Al no ser multiplo, randomiza una letra aleatoria
        message += chr(ascii)           # La añade a la cadena y vuelve a intentarlo
        
    for char in message:                # Recorremos los caracteres del mensaje
        LISTA_TMP.append(ord(char))     # Los ingreasmos a una lista convertidos en ASCII
        
    output=[LISTA_TMP[i:i + 3] for i in range(0, len(LISTA_TMP), 3)] # 'Parseamos' a una matriz
    return output

# Contruimos la matriz clave con números aleatorios
def matriz_keygen(size):
    matriz_clave = []
    LISTA_TMP = []
    # Relleno una lista con tantos valores aleatorios como elementos a rellenar en la matriz determinada por size (size * size)
    for x in range(size * size):
        LISTA_TMP.append(random.randrange(40))
    # Se crea la matrix clave con los valores generados, de tamaño size * size
    matriz_clave = np.array(LISTA_TMP).reshape(size, size)
    return matriz_clave

# Con esta funcion multiplicamos y encriptamos los datos
def encript(message, size):
    
    x = matrizFrase(message) # Obtenemos la matriz de la frase
    y = matriz_keygen(size)  # Obtenemos la matriz clave
    
    r = np.matmul(x,y)       # Las multiplicamos
    output = np.array(r)     # La convertimos en un array para poder trabajar mejor
    listEncript = output.flatten()
    result = ''
    for i in listEncript:
        if (i%127)<= 33:
            r = 33
        elif (i%127>=126):
            r = 126
        else:
            r = i%127   
        result += chr(r)
    return result    

if __name__ == '__main__':
    
    
    print(Color.BLUE+''' 
                     ##########################################################
                     #                  CIFRADO HILL ROBUSTO                  #
                     ##########################################################   
                    '''+'\n')
    while True:
        print('[1] ENCRIPTAR MENSAJE')
        print('[2] DESENCRIPTAR MENSAJE') # No esta implementado
        print('[3] EXIT'+'\n')
        opcion = int(input('>>> '))
        if opcion == 1:
            message = input(Color.DARKCYAN+'Escribe un mensaje a cifrar: ')
            print('\n'+Color.PURPLE+'La frase encriptada es: '+encript(message,3)+'\n')
        elif opcion == 2:
            if message == '':
                print(Color.RED+'MENSAJE VACIO!!!')
            else:
                print(Color.GREEN+'No se puede desencriptar. Funcion no implementada')
        elif opcion == 3:
            break    
            
            
            
            
    
