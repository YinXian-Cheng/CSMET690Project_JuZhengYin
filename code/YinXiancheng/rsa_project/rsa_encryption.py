def encrypt_message_rsa(message, public_key):
    """
    Encrypts a message using RSA encryption.

    Args:
    message: The message to encrypt, represented as an integer.
    public_key: A tuple containing (e, n), the RSA public key components.

    Returns:
    The encrypted message.
    """
    if not isinstance(message, int) or message < 0:
        raise ValueError("Invalid message: must be a non-negative integer")
    e, n = public_key

    # Encrypt the message
    encrypted_message = pow(message, e, n)

    print("Message encrypted.")
    return encrypted_message

# Example usage
if __name__ == "__main__":
    # Assume we have the RSA public key (e, n)
    # For demonstration, replace these with actual values from the public key file
    e = 65537  # Example public exponent
    n = 999027  # Example modulus (this should be replaced with the actual n)

    public_key = (e, n)

    # Message to be encrypted
    message = 123456  # Example message

    # Encrypt the message
    encrypted_message = encrypt_message_rsa(message, public_key)
    print("Encrypted Message:", encrypted_message)
