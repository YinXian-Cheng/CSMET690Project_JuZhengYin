# ElGamal_Generate_Hacker.py

import time

def brute_force_dlp_with_timeout(g, h, p, timeout):
    """Attempt to solve the discrete logarithm problem g^x = h (mod p) by brute force method, but there is a time limit"""
    start_time = time.time()
    for x in range(1, p):
        if time.time() - start_time > timeout:
            return None  # Give up after timeout
        if pow(g, x, p) == h:
            return x
    return None

def elgamal_hack(p, g, public_key, c1, c2, timeout):
    """Attempt to crack ElGamal encryption, but there is a time limit"""
    # Try to find the private key via brute force method
    private_key = brute_force_dlp_with_timeout(g, public_key, p, timeout)
    if private_key is None:
        return "Failed to find private key within the given time limit"

    # Decrypt using the found private key
    s = pow(c1, private_key, p)
    s_inverse = pow(s, p - 2, p)  # Compute the inverse of s
    m = (c2 * s_inverse) % p
    return m

def main():
    # user input
    p = int(input("Enter the prime number (p): "))
    g = int(input("Enter the primitive root of p (g): "))
    public_key = int(input("Enter the public key: "))
    c1 = int(input("Enter the first part of the encrypted message (c1): "))
    c2 = int(input("Enter the second part of the encrypted message (c2): "))
    timeout = int(input("Enter the time limit in seconds for the hacking attempt: "))

    # try to crack
    decrypted_message = elgamal_hack(p, g, public_key, c1, c2, timeout)

    # Output cracking results
    output = f"Attempted Decryption (Eve's perspective): {decrypted_message}"
    print(output)

    # Save output to file
    with open("ElGamal_hacker_Information.txt", 'w') as file:
        file.write(output)

if __name__ == "__main__":
    main()
