import argparse
import time
from rsa_decryption import decrypt_message_rsa


def factorize_n(n):
    """ Simple and inefficient factorization just for demonstration purposes. """
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None, None


def main():
    parser = argparse.ArgumentParser(description='RSA Decryption Attempt (Eve)')
    parser.add_argument('encrypted_file', type=str, help='File containing the encrypted message')
    args = parser.parse_args()

    # Read the public key (e, n) from the file
    with open('rsa_public_key.txt', 'r') as file:
        e_str, n_str = file.read().split(',')
        e, n = int(e_str), int(n_str)

    print("RSA public key (e, n) got by Eve:", e, n)

    # Read the encrypted message from the specified file
    with open(args.encrypted_file, 'r') as file:
        encrypted_message = int(file.read())

    print("Encrypted message got by Eve:", encrypted_message)

    # Set a time limit for Eve's brute-force attempt (e.g., 10 seconds)
    time_limit = 10  # in seconds
    start_time = time.time()

    # Eve tries to factorize n to find p and q
    p, q = factorize_n(n)
    if p is not None and q is not None:
        phi_n = (p - 1) * (q - 1)
        d = pow(e, -1, phi_n)  # Compute the private exponent
        decrypted_message = decrypt_message_rsa(encrypted_message, (d, n))
        print("Guessed private keys:", p, "*", q, "=", p*q, "\n", "Computed Private Exponent (d):", d, "\n", "Eve's Successful Guess: Decrypted Message:", decrypted_message)
    else:
        print("Failed to factorize n within the time limit.")


if __name__ == "__main__":
    main()
