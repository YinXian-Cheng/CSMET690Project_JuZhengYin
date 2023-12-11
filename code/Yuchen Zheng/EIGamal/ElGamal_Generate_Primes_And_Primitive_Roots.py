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
    """ Find a primitive root for prime p """
    if p == 2:
        return 1

    # Function to find all prime factors of a given number n
    def find_prime_factors(n):
        prime_factors = set()
        # Count the number of 2s that divide n
        while n % 2 == 0:
            prime_factors.add(2)
            n //= 2
        # n must be odd at this point, so a skip of 2 is used (i.e., i = i + 2)
        for i in range(3, int(n**0.5) + 1, 2):
            # While i divides n, add i and divide n
            while n % i == 0:
                prime_factors.add(i)
                n //= i
        # If n is a prime number greater than 2
        if n > 2:
            prime_factors.add(n)
        return prime_factors

    # Find prime factors of p-1
    prime_factors = find_prime_factors(p - 1)


    # Test potential g's using random selection
    tested_g_values = set()
    while True:
        g = random.randint(2, p - 1)
        if g in tested_g_values:  # Skip if this g has already been tested
            continue
        tested_g_values.add(g)

        if all(pow(g, (p - 1) // factor, p) != 1 for factor in prime_factors):
            return g

# Generating a large prime p and its primitive root g
p = generate_large_prime(60)
g = find_primitive_root(p)

# Writing to a file
file_name = "ElGamal_number_and_root.txt"
with open(file_name, 'w') as file:
    file.write(f"Prime number (p): {p}\n")
    file.write(f"Primitive root (g): {g}")
