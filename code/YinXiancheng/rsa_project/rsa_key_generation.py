import random
from sympy import nextprime, isprime, gcd


def generate_prime(starting_value):
    """Generate a large prime number."""
    starting_value = (random.randint(2 ** 30, 2 ** 31))
    prime = nextprime(starting_value)
    while not isprime(prime):
        prime = nextprime(prime)
    return prime


def generate_rsa_keys():
    # Generate two distinct primes p and q
    p = generate_prime(random.randint(2 ** 30, 2 ** 31))
    q = generate_prime(p)
    while q == p:
        q = generate_prime()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose e, 65537 is a common choice for e
    e = 65537
    while gcd(e, phi_n) != 1:
        e += 2  # increment e until it is coprime to phi_n

    # Compute d, the mod inverse of e
    d = pow(e, -1, phi_n)

    return (e, n), (d, n)  # Return public and private keys


# Generate RSA keys
public_key, private_key = generate_rsa_keys()

# Save the public key (e, n) to a file
with open('rsa_public_key.txt', 'w') as file:
    file.write(f"{public_key[0]},{public_key[1]}")

# Save the private key (d, n) to a file
with open('rsa_private_key.txt', 'w') as file:
    file.write(f"{private_key[0]},{private_key[1]}")

print("RSA keys generated and saved to files""rsa_public_key.txt"" and ""rsa_private_key.txt""", "\n", "public_key:", public_key, "private_key:", private_key)
