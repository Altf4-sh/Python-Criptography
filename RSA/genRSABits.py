# Generador de números primos para el cifrado RSA
import random

def is_probably_prime(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for i in range(k):
        x = pow(random.randint(2, n-1), d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_probably_prime(p):
            return p
        
if __name__ == '__main__':
    
    print(generate_prime(2048))