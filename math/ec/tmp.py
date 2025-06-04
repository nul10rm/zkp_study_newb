from py_ecc.bn128 import G1, neg, multiply

field_modulus = 21888242871839275222246405745257275088696311157297823662689037894645226208583
for i in range(1, 4):
    point = multiply(G1, i)
    print(point)
    print(neg(point))
    print('----')

    # x values are the same
    assert int(point[0]) == int(neg(point)[0])

    # just a integer addition
    assert int(point[1]) + int(neg(point)[1]) == field_modulus

