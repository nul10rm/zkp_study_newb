from py_ecc.bn128 import G1, G2, eq, curve_order, multiply
x = 10
assert eq(multiply(G2, x + curve_order), multiply(G2, x))
assert eq(multiply(G1, x + curve_order), multiply(G1, x))