import argparse
from rsa_decryption import decrypt_message_rsa


def main():
    parser = argparse.ArgumentParser(description='RSA Decryption (Bob)')
    parser.add_argument('encrypted_file', type=str, help='File containing the encrypted message')
    args = parser.parse_args()

    # Get the private key
    with open('rsa_private_key.txt', 'r') as file:
        d_str, n_str = file.read().split(',')
        d, n = int(d_str), int(n_str)

    print("RSA private key of Bob:", d, ",", n)

    # Read the encrypted message from the specified file
    with open(args.encrypted_file, 'r') as file:
        encrypted_message = int(file.read())

    print("Encrypted message got:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message_rsa(encrypted_message, (d, n))

    # Bob reads the decrypted message
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()
