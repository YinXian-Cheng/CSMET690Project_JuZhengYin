# RSA_Generates_Encrypted_Information.py

def rsa_encrypt(public_key, modulus, message):
    """Encrypt a message using RSA encryption."""
    # Convert the message to an integer
    message_as_int = int.from_bytes(message.encode('utf-8'), 'big')

    # Encrypt the message
    # ciphertext = (message_as_int ** public_key) % modulus
    ciphertext = pow(message_as_int, public_key, modulus)
    return ciphertext

def main():
    # User input for public key exponent and modulus
    public_key = int(input("Enter the public key exponent (e): "))
    modulus = int(input("Enter the modulus (n): "))
    message = input("Enter the message to encrypt (M): ")

    # Encrypt the message
    encrypted_message = rsa_encrypt(public_key, modulus, message)

    # Write the encrypted message to a file
    with open('RSA_Encrypted_Information.txt', 'w') as f:
        f.write(f"Encrypted Message: {encrypted_message}\n")

    print("Encrypted message generated and saved to RSA_Encrypted_Information.txt")

if __name__ == "__main__":
    main()
