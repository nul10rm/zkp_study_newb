# provided by prob
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
###################################################################

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

def sqrt(t):
    p = pow(t, (q+1)//4, q)
    return p, q - p

# -------- Solves ---------
a = 497
b = 1768
q = 9739
G = (1804, 5368)

x = 4726

(y1, y2) = sqrt((x ** 3 + a * x + b) % q)
P = (x, y1) # y값에 상관없이 x값은 항상 같음
RES = scalar_multiplication(6534, P)

shared_secret = RES[0]
iv = 'cd9da9f1c60925922377ea952afc212c'
encrypted_flag = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv=iv, ciphertext=encrypted_flag))

