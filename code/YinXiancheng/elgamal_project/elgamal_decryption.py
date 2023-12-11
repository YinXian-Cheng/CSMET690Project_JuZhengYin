from sympy import mod_inverse


def decrypt_message(encrypted_message, private_key, p):
    """
    Decrypts an encrypted message using ElGamal decryption.

    Args:
    encrypted_message: A tuple containing (A, X), the encrypted message.
    private_key: The private key 'b' used for decryption.
    p: The prime number used in the ElGamal encryption.

    Returns:
    The decrypted message M.
    """
    A, X = encrypted_message
    s = pow(A, private_key, p)  # Shared secret s = A^b mod p
    s_inv = mod_inverse(s, p)   # Inverse of s mod p
    M = (X * s_inv) % p         # M = X * s^-1 mod p

    return M
