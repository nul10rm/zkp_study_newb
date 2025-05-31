from libnum import has_sqrtmod_prime_power, sqrtmod_prime_power

# has_sqrtmod_prime_power(n, field_mod, k), where n**k,
print(has_sqrtmod_prime_power(8, 11, 1))

print(has_sqrtmod_prime_power(5, 11, 1))

print(list(sqrtmod_prime_power(5, 11, 1)))

# sqrt는 두 개의 해를 가지므로, 두 개의 답이 존재함.
assert (4 ** 2) % 11 == 5
assert (7 ** 2) % 11 == 5

assert (4 + 7) % 11 == 0