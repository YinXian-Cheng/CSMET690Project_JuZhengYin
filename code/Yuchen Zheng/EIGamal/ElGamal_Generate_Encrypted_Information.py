# ElGamal_Generate_Encrypted_Information.py

import random

def elgamal_encrypt(public_key, p, g, message):
    # ElGamal encryption process
    y = public_key

    # Since the message is already a numeric string, convert it directly to an integer
    m = int(message)

    # Generate random number k
    k = random.randint(1, p - 2)

    # Calculate c1 and c2
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p

    return c1, c2

def main():
    # User input
    public_key = int(input("Enter the public key: "))
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root of p (g): "))
    message = input("Enter the message to encrypt: ")

    # Perform ElGamal encryption
    c1, c2 = elgamal_encrypt(public_key, p, g, message)

    # Output encryption result
    output = f"Encrypted Message Part 1 (c1): {c1}\nEncrypted Message Part 2 (c2): {c2}"
    print(output)

    # Save output to file
    with open("ElGamal_encrypted_Information.txt", 'w') as file:
        file.write(output)

if __name__ == "__main__":
    main()

