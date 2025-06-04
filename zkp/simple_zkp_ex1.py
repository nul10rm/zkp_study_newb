from py_ecc.bn128 import G1, curve_order, multiply, add

secret = 7
pub = [23, 161]

public_input = pub[0]
secret_input = multiply(G1, secret)

proof = [public_input, secret_input, pub[1]]

assert multiply(proof[1], proof[0]) == multiply(G1, proof[2])
print("Proof success") 

'''
a + b = 15G.
This type of zkp is not a true zkp
attacker can generate arbitrary inputs that fits to the result.
'''