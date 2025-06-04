from py_ecc.bn128 import G1, multiply, add

secret_x = 5 
secret_y = 10

x = multiply(G1, 5)
y = multiply(G1, 10)

proof = (x, y, 15)

assert multiply(G1, proof[2]) == add(proof[0], proof[1])
print("Proof success")