from src.main.prime import *
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        min_length = 20
        max_length = 30
        self.n, self.p, self.q = generate_n(20,30)
        self.phi_n = phi(self.p,self.q)
        self.e = find_coprime_e(self.phi_n)
        self.d, _ = inverse_euclidean_d(self.phi_n,self.e)

    def test1(self):
        message = 29
        cipher = cryptography(message,self.e,self.n)
        decrypted = decryption(cipher,self.d,self.n)
        self.assertEqual(message,decrypted)

    def test2(self):
        message = 187
        cipher = cryptography(message,self.e,self.n)
        decrypted = decryption(cipher,self.d,self.n)
        self.assertEqual(message,decrypted)

    def test3(self):
        message = 7039
        cipher = cryptography(message,self.e,self.n)
        decrypted = decryption(cipher,self.d,self.n)
        self.assertEqual(message,decrypted)