import random
from prime import generate_prime_number

p = 0
q = 0

def generate_n():
    min_length = 40
    max_length = 50

    length = random.randint(min_length, max_length)
    global p
    p = generate_prime_number(length)

    length = random.randint(min_length, max_length)
    global q
    q = generate_prime_number(length)

    n = p * q
    return n

def phi():
    if p == 0 or q == 0:
        return -1
    return (p-1)*(q-1)