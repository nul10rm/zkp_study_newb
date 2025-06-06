a = 497
b = 1768
modular = 9739

def point_addition(P, Q):
    if P[0] == P[1] == None:
        return (Q[0], Q[1])
    elif Q[0] == Q[1] == None:
        return (P[0], P[1])
    
    if (P[0] == Q[0] and P[1] == -Q[1]):
        return (None, None)
    
    sigma = 0
    if (P == Q):
        sigma = (3 * P[0] ** 2 + a) * pow(2 * P[1], -1, modular) % modular
    else:
        sigma = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, modular) % modular
    
    res_x = (sigma ** 2 - P[0] - Q[0]) % modular
    res_y = (sigma * (P[0] - res_x) - P[1]) % modular

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


# -------- point_addition_prob --------
P = (493, 5564)
Q  = (1539, 4742)
R = (4403, 5202)

tmp1 = point_addition(P, P)
tmp2 = point_addition(tmp1, Q)
print(point_addition(tmp2, R))
# ans = (4215, 2162)

# -------- scalar multiplication --------
n = 1337
X = (5323, 5438)
print(scalar_multiplication(n, X))

n = 7863
P = (2339, 2213)
print(scalar_multiplication(n, P))
# ans = (9467, 2742)

# -------- Curves and Logs --------

