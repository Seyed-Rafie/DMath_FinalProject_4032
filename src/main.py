import random
from prime import generate_prime_number

def generate_n():
    min_length = 40
    max_length = 50

    length = random.randint(min_length, max_length)
    p = generate_prime_number(length)

    length = random.randint(min_length, max_length)
    q = generate_prime_number(length)

    n = p * q
    return n