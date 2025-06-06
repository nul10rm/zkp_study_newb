from math import sqrt

a = 497
b = 1768
q = 9739
G = (1804, 5368)

def point_addition(P, Q):
    if P[0] == P[1] == None:
        return (Q[0], Q[1])
    elif Q[0] == Q[1] == None:
        return (P[0], P[1])
    
    if (P[0] == Q[0] and P[1] == -Q[1]):
        return (None, None)
    
    sigma = 0
    if (P == Q):
        sigma = (3 * P[0] ** 2 + a) * pow(2 * P[1], -1, q) % q
    else:
        sigma = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, q) % q
    
    res_x = (sigma ** 2 - P[0] - Q[0]) % q
    res_y = (sigma * (P[0] - res_x) - P[1]) % q

    return (res_x, res_y)

def scalar_multiplication(n, P):
    Q = P
    R = (None, None)

    while n > 0:
        if (n % 2 == 1):
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n //= 2
    
    return R

def sqrt(x):
    for i in range(1, q):
        if pow(i, 2, q) == x:
            return (i, q-i)
    return None 

# -------- Solves ---------
x = 4726
(y1, y2) = sqrt(pow(x, 3) + a * x + b) % q
P = (x, y)
print(scalar_multiplication(6534, P))