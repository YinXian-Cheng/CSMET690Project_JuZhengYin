import argparse
from elgamal_encryption import encrypt_message


def main():
    parser = argparse.ArgumentParser(description="ElGamal Encryption (Alice)")
    parser.add_argument("message", type=int, help="Message to be encrypted (as an integer)")
    args = parser.parse_args()

    # Alice gets Bob's public key (p, g, B)
    with open('elgamal_public_keys.txt', 'r') as file:
        p_str, g_str, B_str = file.read().split(',')
        p, g, B = int(p_str), int(g_str), int(B_str)

    print("Public keys got by Alice:", p, ",", g, ",", B)

    public_key = (p, g, B)

    # Encrypt the message
    encrypted_message = encrypt_message(args.message, public_key)

    # Send the message (Write the encrypted message to file 'elgamal_encrypted_message.txt')
    with open('elgamal_encrypted_message.txt', 'w') as file:
        file.write(f"{encrypted_message[0]},{encrypted_message[1]}")

    print("Message sent by Alice. Encrypted Message:", encrypted_message)


if __name__ == "__main__":
    main()
