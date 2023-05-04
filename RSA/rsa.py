'''
Algoritmo RSA a pulmón.

Pasos:
    - Elegir dos números aleatorios p y q del fichero proporcionado.
    - Calculamos el número de Euler phi con p y q. N = (p-1)*(q-1)
    - Se pedira una clave publica mayor que 1 y menor que phi llamado e. Se tiene que cumplir -> mcd (e,phi) = 1
    - Para obtener la clave privada hay que hacer el algoritmo extendido de Euclides. inv (e, phi)
    - Enviamos un número secreto x calculando c. c= n^e mod phi (de la otra persona).
    - La otra persona puede recuperar ese número calculando -> N = C^(su clave privada) mod phi(tuyo)
    - Para intentar romper este cifrado vamos a usar la factorizacion
    - 
'''

# IMPORTS NECESARIOS
import random
import numpy
from time import sleep
import math
import gmpy2

# ESTILOS COLORES
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

'''************************************************************************************'''
# Ataque RSA
def factorizar(n):
    """
    Factoriza el número 'n' en dos números primos.
    """
    p = gmpy2.next_prime(gmpy2.isqrt(n))
    while True:
        q, r = divmod(n, p)
        if r == 0:
            return p, q
        p = gmpy2.next_prime(p)

def ataque_rsa(e, n):
    """
    Realiza un ataque por factorización al cifrado RSA con clave pública (e, n).
    Devuelve el valor de la clave privada.
    """
    p, q = factorizar(n)
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    return d


# FUNCION RSA
def RSA():
    
    with open('primos-desde 40k hasta-100k.txt', 'r') as file: # Abrimos el fichero en modo lectura
        lines = file.readlines()                               # Leemos linea a linea
        P1 = int(random.choice(lines))                              # Con esta funcion escogemos un numero elemento aleatorio del fichero        
        P2 = int(random.choice(lines))
        Q1 = int(random.choice(lines))
        Q2 = int(random.choice(lines))
        while True:
            if Q1 == P1:
                Q1 = int(random.choice(lines))
            elif Q2 == P2:
                Q2 = int(random.choice(lines))
            else:
                break
        
    file.close()
    sleep(1)
    print(f'Primos seleccionados >>> P1 = {P1}, Q1 = {Q1}, P2 = {P2}, Q2 = {Q2}'+'\n')
    # Calculamos N y PHI
    N1 = P1 * Q1
    N2 = P2 * Q2
    PHI_1 = (P1-1) * (Q1-1)
    PHI_2 = (P2-1) * (Q2-1)
    
    print(Color.PURPLE+f'El resultado de la operacion >>> N1 = P1 * Q1 = {N1}')
    sleep(0.5)
    print(f'El resultado de la operacion >>> N2 = P2 * Q2 = {N2}')
    sleep(0.5)
    print(f'El resultado de la operacion >>> PHI_1 = (P1-1) * (Q1-1) = {PHI_1}')
    sleep(0.5)
    print(f'El resultado de la operacion >>> PHI_2 = (P2-1) * (Q2-1) = {PHI_2}')
    
    E1 = 0
    E2 = 0
    print('PROCESS...'+'\n')
    while (math.gcd(E1, PHI_1) != 1):
        E1 = random.randint(1,PHI_1)
    while (math.gcd(E2, PHI_2) != 1):    
        E2 = random.randint(1,PHI_2)
    sleep(1)
    print(Color.BOLD+f'La clave pública E1 = {E1} y la clave pública E2 = {E2}'+'\n')
    
    print('OBTENIENDO LA CLAVE PRIVADA...'+'\n')
    sleep(2)
    D1 = inverso_modular(E1,PHI_1)
    D2 = inverso_modular(E2, PHI_2)

    sleep(1)
    cifra = input('Ingresa un número para cifrar: ')
    print(Color.YELLOW+'CIFRANDO MENSAJE...')
    sleep(2)
    mensaje_cifrado = [pow(ord(c), E2, N2) for c in cifra]
    print(f'Mensaje cifrado >>> {mensaje_cifrado}'+'\n')
    sleep(2)
    
    print('ATACANDO RSA A N1...')
    OK = ataque_rsa(E1,N1)
    print(f'Ataque exitoso. Clave privada de N1 >>> {OK}'+'\n')
    
    print('ATACANDO RSA A N2...')
    OK2 = ataque_rsa(E2,N2)
    print(f'Ataque exitoso. Clave privada de N2 >>> {OK2}'+'\n')
    
    
    sleep(2)
    print('DESCIFRANDO MENSAJE...')
    mensaje_descifrado = [chr(pow(c, D2, N2)) for c in mensaje_cifrado]
    print(f'El mensaje decía >>> {mensaje_descifrado}'+'\n')
    
    
# INVERSO MULTIPLICATIVO DE E Y PHI  
def inverso_modular(e, phi):
    """
    Calcula el inverso modular de 'e' módulo 'phi' utilizando el algoritmo
    extendido de Euclides.
    """
    r1, r2 = e, phi
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    
    while r2 > 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
        
    if r1 == 1:
        return s1 % phi
    else:
        return None
    
    
if __name__ == '__main__':
    
    print(Color.GREEN+''' 
                    ##########################################################
                    #                  CIFRADO RSA A PULMON                  #
                    ##########################################################   
                '''+'\n')
    print('RUNNING...')
    sleep(1)
    RSA()











