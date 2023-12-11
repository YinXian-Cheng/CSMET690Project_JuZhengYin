import random
from sympy import isprime, nextprime


# Global variables
p, g, B, b = None, None, None, None


def generate_prime(starting_value=(random.randint(2**30, 2**31))):
    """Generate a large prime number."""
    prime = nextprime(starting_value)
    while not isprime(prime):
        prime = nextprime(prime)
    return prime


def generate_keys():
    """Generate ElGamal public and private keys."""
    global p, g, B, b
    p = generate_prime()
    g = nextprime(random.randint(2, 100))  # Simplified choice for g
    b = random.randint(1, p - 1)  # Private key
    B = pow(g, b, p)  # Public key component
    # Write public keys to a file
    with open('elgamal_public_keys.txt', 'w') as file:
        file.write(f"{p},{g},{B}")
    return p, g, B, b


# Generate Bob's keys
p, g, B, b = generate_keys()

# Write private key b to a file that only bob can use
with open('elgamal_private_key_only_accessible_by_bob.txt', 'w') as file:
    file.write(f"{b}")
print("elgamal private key generated:", b, ", stored where only accessible by bob")

# Write public keys to a file for Alice and Eve to use
with open('elgamal_public_keys.txt', 'w') as file:
    file.write(f"{p},{g},{B}")
print("elgamal public keys generated:"," prime:",p,"next prime:", g, "public key component:", B, ", accessible by alice, bob, eve")
