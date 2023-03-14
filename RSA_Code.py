'''

1. pick two prime numbers : p and q <-- x
2. n = p * q
3. phi_n = (p-1)(q-1)
4. pick random e prime with phi_n (pgcd(e, phi_n) = 1)
5. public key: (e, n)
6. pick d : (e * d) % phi_n = 1
7. private key : (d, n)  

---- 

encryption

C = (M ^ e) % n

decryption

M = (C ^ d) % n

'''
import random

with open('primes.txt', 'r') as file:
    lines = file.readlines()
    numbers = [int(x.strip()) for x in lines]   # convert each line to integer and store in list

# 1

p = random.choice(numbers)

q = random.choice(numbers)

# 2

n = p*q

# 3

phi_n = (p-1)*(q-1)

# 4

e = random.randint(1, 100)

if (e % phi_n ==1) :
  True
else :
  e = random.randint(1, 100)

# 5

print(p)
print(q)