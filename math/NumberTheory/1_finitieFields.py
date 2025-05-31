import galois

GF7 = galois.GF(7)

one_half = GF7(1) / GF7(2)
one_third = GF7(1) / GF7(3)
five_over_six = GF7(5) / GF7(6)

inv_one = GF7(1) / GF7(5)
print(inv_one)

assert one_half + one_third == five_over_six