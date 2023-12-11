import random


def encrypt_message(message, public_key):
    """
    Encrypts a message m using ElGamal encryption.

    Args:
    m: The message to encrypt, represented as an integer.
    public_key: A tuple containing (p, g, B), Bob's public key components.

    Returns:
    A tuple of the form (A, X), the encrypted message.
    """
    if not isinstance(message, int) or message < 0:
        raise ValueError("Invalid message: must be a non-negative integer")
    p, g, B = public_key
    a = random.randint(1, p - 2)  # Alice's random number a
    s = pow(B, a, p)  # Shared secret s = B^a mod p
    A = pow(g, a, p)  # A = g^a mod p
    X = (message * s) % p  # X = m * s mod p
    print("message encrypted.")
    return A, X
