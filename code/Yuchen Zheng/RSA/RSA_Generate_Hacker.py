# RSA_Generate_Hacker.py

import time

def attempt_prime_factorization(n, time_limit=10):
    """Try to decompose n within a limited time."""
    start_time = time.time()
    i = 2
    while i * i <= n:
        if time.time() - start_time > time_limit:
            return None
        if n % i:
            i += 1
        else:
            return i, n // i
    return None

def main():
    # The user inputs the modulus n, the public key exponent e and the encrypted message M'
    n = int(input("Enter the modulus (n): "))
    e = int(input("Enter the public key exponent (e): "))
    encrypted_message = int(input("Enter the encrypted message (M'): "))

    # Try factorizing modulo n
    factors = attempt_prime_factorization(n)

    # Write results to file
    with open('RSA_Hacker_Information.txt', 'w') as f:
        if factors:
            f.write(f"Success! Factors of n found: {factors}\n")
        else:
            f.write("Failed to crack RSA encryption within the time limit.\n")
            f.write("This demonstrates the difficulty of breaking RSA encryption ")
            f.write("due to the computational challenge of factoring large numbers.\n")

    print("Result saved to RSA_Hacker_Information.txt")

if __name__ == "__main__":
    main()
