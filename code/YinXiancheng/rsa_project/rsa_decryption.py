def decrypt_message_rsa(encrypted_message, private_key):
    """
    Decrypts an encrypted message using RSA decryption.

    Args:
    encrypted_message: The encrypted message, represented as an integer.
    private_key: A tuple containing (d, n), the RSA private key components.

    Returns:
    The decrypted message.

    pow() is used, which uses an optimized algorithm for modular exponentiation.
    It is significantly faster than simply computing (encrypted_message ** d) % n
    """
    d, n = private_key

    # Decrypt the message
    decrypted_message = pow(encrypted_message, d, n)

    return decrypted_message
