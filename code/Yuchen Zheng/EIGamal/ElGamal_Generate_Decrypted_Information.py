# ElGamal_Generate_Decrypted_Information.py

def elgamal_decrypt(private_key, p, c1, c2):
    # ElGamal decryption process
    s = pow(c1, private_key, p)
    s_inverse = pow(s, p - 2, p)  # Compute the inverse of s using Fermat's Little Theorem
    m = (c2 * s_inverse) % p
    return str(m)

def main():
    # user input
    private_key = int(input("Enter the private key: "))
    p = int(input("Enter a prime number (p): "))
    c1 = int(input("Enter the first part of the encrypted message (c1): "))
    c2 = int(input("Enter the second part of the encrypted message (c2): "))

    # Perform ElGamal decryption
    decrypted_message = elgamal_decrypt(private_key, p, c1, c2)

    # Output decryption result
    output = f"Decrypted Message: {decrypted_message}"
    print(output)

    # Save output to file
    with open("ElGamal_decryption_Information.txt", 'w') as file:
        file.write(output)

if __name__ == "__main__":
    main()

