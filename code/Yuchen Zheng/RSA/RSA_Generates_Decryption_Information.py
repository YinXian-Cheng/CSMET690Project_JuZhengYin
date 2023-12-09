# RSA_Generates_Decryption_Information.py

def rsa_decrypt(private_key, modulus, ciphertext):
    """Decrypt a message using RSA decryption."""
    # Decrypt the message
    decrypted_message_as_int = pow(ciphertext, private_key, modulus)

    # Convert the message back to string
    decrypted_message = decrypted_message_as_int.to_bytes(
        (decrypted_message_as_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return decrypted_message

def main():
    # User input for private key exponent and modulus
    private_key = int(input("Enter the private key exponent (d): "))
    modulus = int(input("Enter the modulus (n): "))
    encrypted_message = int(input("Enter the encrypted message (M'): "))

    # Decrypt the message
    decrypted_message = rsa_decrypt(private_key, modulus, encrypted_message)

    # Write the decrypted message to a file
    with open('RSA_Decryption_Information.txt', 'w') as f:
        f.write(f"Decrypted Message: {decrypted_message}\n")

    print("Decrypted message generated and saved to RSA_Decryption_Information.txt")

if __name__ == "__main__":
    main()
