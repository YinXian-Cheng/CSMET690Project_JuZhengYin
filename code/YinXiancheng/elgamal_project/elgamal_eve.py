import argparse
import time
from elgamal_decryption import decrypt_message


def main():
    parser = argparse.ArgumentParser(description='ElGamal Decryption Attempt (Eve)')
    parser.add_argument('encrypted_file', type=str, help='File containing the encrypted message')
    args = parser.parse_args()

    # Read the public keys from the file
    with open('elgamal_public_keys.txt', 'r') as file:
        p_str, g_str, B_str = file.read().split(',')
        p, g, B = int(p_str), int(g_str), int(B_str)

    public_key = (p, g, B)
    print("Public key of Bob got by Eve:", public_key)

    # Read the encrypted message from the file specified in the command
    with open(args.encrypted_file, 'r') as file:
        A_str, X_str = file.read().split(',')
        A, X = int(A_str), int(X_str)

    encrypted_message = (A, X)
    print("Encrypted message got by Eve:", encrypted_message)

    # Set a time limit for Eve's brute-force attempt (e.g., 10 seconds)
    time_limit = 10  # in seconds
    start_time = time.time()

    # Eve tries different private keys to decrypt the message
    for potential_private_key in range(1, p):
        if time.time() - start_time > time_limit:
            print("Time limit reached, stopping brute-force attempt")
            break

        try:
            decrypted_message = decrypt_message(encrypted_message, potential_private_key, p)
            print("Eve's Guess:", decrypted_message)
        except Exception as e:
            pass  # Eve ignores errors and keeps trying


if __name__ == '__main__':
    main()
