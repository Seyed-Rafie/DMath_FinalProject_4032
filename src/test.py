from prime import inverse_euclidean_d

p = 61
q = 53

phi_n = 60 * 52
e = 17

a , _ = inverse_euclidean_d(phi_n, e)
d = a % phi_n
print(d) # 2753 = true