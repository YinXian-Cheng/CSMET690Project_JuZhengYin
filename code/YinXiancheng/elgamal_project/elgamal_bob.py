import argparse
from elgamal_decryption import decrypt_message


def main():
    parser = argparse.ArgumentParser(description="ElGamal Decryption (Bob)")
    parser.add_argument("A", type=int, help="Encrypted Message Part 1 (A)")
    parser.add_argument("X", type=int, help="Encrypted Message Part 2 (X)")
    args = parser.parse_args()

    # Get the private key
    with open('elgamal_private_key_only_accessible_by_bob.txt', 'r') as file:
        m_str = file.read()
        m = int(m_str)

    print("private key m of bob:", m)

    with open('elgamal_public_keys.txt', 'r') as file:
        p_str, g_str, B_str = file.read().split(',')
        p, g, B = int(p_str), int(g_str), int(B_str)

    print("public key of bob:", p, ",", g, ",", B)

    encrypted_message = (args.A, args.X)  # Use values from command line arguments

    print("Encrypted message got:", args.A, ",", args.X)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, m, p)

    # Bob reads the decrypted message
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()
