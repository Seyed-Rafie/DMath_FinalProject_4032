#in the name of GOD
import random
import math


def generate_prime_number(length):
    while True:
        n = random.randint(10**(length-1), 10**length)
        if is_prime(n):
            return n



def is_prime(n): # with Miller Rabbin algorithm

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    k = 40
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_n(min_length, max_length):

    length = random.randint(min_length, max_length)
    global p
    p = generate_prime_number(length)

    length = random.randint(min_length, max_length)
    global q
    q = generate_prime_number(length)

    n = p * q
    return n,p,q

def phi(p,q):
    if p == 0 or q == 0:
        return -1
    return (p-1)*(q-1)

def find_coprime_e(phi_n):
    
    for candidate in [65537, 257, 17, 5, 3]:  #Fermat Numbers(standard for RSA)
        if candidate < phi_n and math.gcd(candidate, phi_n) == 1:
            return candidate
    
    while True:
        candidate = random.randint(7, phi_n - 1)
        if math.gcd(candidate, phi_n) == 1:
            return candidate



def inverse_euclidean_d(phi_n, e):
    if phi_n < e:
        phi_n , e = e , phi_n
    if e == 0:
        return 0, 1
    a,b = inverse_euclidean_d(phi_n % e, e)
    return b - (phi_n//e) * a ,a

def cryptography(message,e,n):
    cipher = pow(message,e, n)
    return cipher

def decryption(cipher,d,n):
    message = pow(cipher, d, n)
    return message
