import argparse
from rsa_encryption import encrypt_message_rsa


def main():
    parser = argparse.ArgumentParser(description='RSA Encryption (Alice)')
    parser.add_argument('message', type=int, help='Message to be encrypted (as an integer)')
    args = parser.parse_args()

    # Alice gets Bob's RSA public key (e, n)
    with open('rsa_public_key.txt', 'r') as file:
        e_str, n_str = file.read().split(',')
        e, n = int(e_str), int(n_str)

    print("RSA public keys got by Alice:", e, ",", n)

    public_key = (e, n)

    # Encrypt the message
    encrypted_message = encrypt_message_rsa(args.message, public_key)

    # Send the message (Write the encrypted message to file 'rsa_encrypted_message.txt')
    with open('rsa_encrypted_message.txt', 'w') as file:
        file.write(f"{encrypted_message}")

    print("Message sent by Alice. Encrypted Message:", encrypted_message)


if __name__ == "__main__":
    main()
