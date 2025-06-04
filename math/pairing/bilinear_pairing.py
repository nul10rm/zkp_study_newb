from py_ecc.bn128 import G1, G2, pairing, multiply, eq

P = multiply(G1, 3)
Q = multiply(G2, 8)

R = multiply(G1, 24)

print(pairing(Q, P))
print(pairing(G2, R))
