# ElGamal_Generate_Private_and_Public_Keys.py

import random

def generate_elgamal_keys(p, g):
    # Generate private key
    private_key = random.randint(1, p - 2)
    # Generate public key
    public_key = pow(g, private_key, p)
    return private_key, public_key

def main():
    # user input
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root of p (g): "))

    # Generate ElGamal private and public keys
    private_key, public_key = generate_elgamal_keys(p, g)

    # Prepare for output
    output = f"ElGamal Private Key: {private_key}\nElGamal Public Key: {public_key}"
    print(output)

    # Save output to file
    with open("ElGamal_private_and_public_keys.txt", 'w') as file:
        file.write(output)

if __name__ == "__main__":
    main()
