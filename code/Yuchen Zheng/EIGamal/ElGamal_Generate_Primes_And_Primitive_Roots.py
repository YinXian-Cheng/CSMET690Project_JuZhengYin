# ElGamal_Generate_Primes_And_Primitive_Roots.py

import random

def is_prime(n, tests=5):
    """ Miller-Rabin primality test. """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(tests):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_large_prime(keysize=1024):
    """ Generate a random large prime number. """
    while True:
        num = random.randrange(2**(keysize-1), 2**keysize)
        if is_prime(num):
            return num

def find_primitive_root(p):
    """ Find a primitive root for prime p. """
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1

    # Test random g's until one is found that is a primitive root mod p
    while True:
        g = random.randint(2, p - 1)
        if pow(g, (p - 1) // p1, p) != 1:
            if pow(g, (p - 1) // p2, p) != 1:
                return g

# Generating a large prime p and its primitive root g
p = generate_large_prime(1024)
g = find_primitive_root(p)

# Writing to a file
file_name = "ElGamal_number_and_root.txt"
with open(file_name, 'w') as file:
    file.write(f"Prime number (p): {p}\n")
    file.write(f"Primitive root (g): {g}")



