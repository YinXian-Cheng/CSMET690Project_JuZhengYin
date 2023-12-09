# RSA_Generates_Public_And_Private_Keys.py

def generate_prime_candidate(length):
    """Generate an odd integer randomly."""
    from random import getrandbits
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def is_prime(n, k=128):
    """Test if a number is prime using Miller-Rabin primality test."""
    from random import randrange
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_number(length=1024):
    """Generate a prime number of given length."""
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Find the multiplicative inverse of e modulo phi."""
    m0 = phi
    y = 0
    x = 1

    if phi == 1:
        return 0

    while e > 1:
        # q is quotient
        q = e // phi
        t = phi

        # phi is remainder now, process same as Euclid's algo
        phi = e % phi
        e = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x

def generate_keys():
    """Generate RSA keys."""
    length = 1024
    p = generate_prime_number(length)
    q = generate_prime_number(length)
    n = p * q
    phi = (p-1) * (q-1)

    e = 65537
    while gcd(e, phi) != 1:
        e += 2

    d = multiplicative_inverse(e, phi)

    return (e, d, n)

# Generate RSA keys
public_key, private_key, n = generate_keys()

# Write keys to a file
with open('RSA_public_and_private_keys.txt', 'w') as f:
    f.write(f"Public Key Exponent (e): {public_key}\n")
    f.write(f"Private Key Exponent (d): {private_key}\n")
    f.write(f"Modulus (n): {n}\n")

# Return a success message
"RSA keys generated and saved to RSA_public_and_private_keys.txt"
