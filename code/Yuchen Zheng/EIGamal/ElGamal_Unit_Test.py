# ElGamal_Unit_Test.py

import unittest
from ElGamal_Generate_Primes_And_Primitive_Roots import generate_large_prime, find_primitive_root, is_prime
from ElGamal_Generate_Private_and_Public_Keys import generate_elgamal_keys
from ElGamal_Generate_Encrypted_Information import elgamal_encrypt
from ElGamal_Generate_Decrypted_Information import elgamal_decrypt
from ElGamal_Generate_Hacker import brute_force_dlp_with_timeout, elgamal_hack

class TestElGamalEncryption(unittest.TestCase):
    
    def test_prime_generation(self):
        # Test if the generated number is a prime
        prime = generate_large_prime(256)  # Smaller size for testing purpose
        self.assertTrue(is_prime(prime), "Generated number is not a prime.")

    def test_primitive_root(self):
        # Test if the generated number is a primitive root of the given prime
        prime = generate_large_prime(256)
        root = find_primitive_root(prime)
        self.assertNotEqual(root, 0, "Primitive root cannot be 0.")
        self.assertNotEqual(root, 1, "Primitive root cannot be 1.")

    def test_key_generation(self):
        # Test if the public and private keys are correctly generated
        p = generate_large_prime(256)
        g = find_primitive_root(p)
        private_key, public_key = generate_elgamal_keys(p, g)
        self.assertIsInstance(private_key, int, "Private key is not an integer.")
        self.assertIsInstance(public_key, int, "Public key is not an integer.")

    def test_encryption_decryption(self):
        # Test the complete encryption and decryption process
        p = generate_large_prime(256)
        g = find_primitive_root(p)
        private_key, public_key = generate_elgamal_keys(p, g)
        original_message = '1234567890'  # Example message (numeric)
        c1, c2 = elgamal_encrypt(public_key, p, g, original_message)
        decrypted_message = elgamal_decrypt(private_key, p, c1, c2)
        self.assertEqual(original_message, decrypted_message, "Decrypted message does not match the original.")

    def test_hacker_module(self):
        # Test the hacker module's ability to decrypt a message
        p = generate_large_prime(256)
        g = find_primitive_root(p)
        private_key, public_key = generate_elgamal_keys(p, g)
        original_message = '1234567890'
        c1, c2 = elgamal_encrypt(public_key, p, g, original_message)
        hacked_message = elgamal_hack(p, g, public_key, c1, c2, 5)
        if hacked_message is not None:
            self.assertEqual(original_message, str(hacked_message), "Hacked message does not match the original.")
        else:
            self.assertIsNone(hacked_message, "Hacking should either return None or the correct message.")

    # Additional tests
    def test_small_prime_generation(self):
        small_prime = generate_large_prime(16)
        self.assertTrue(is_prime(small_prime), "Small prime generation failed.")

    def test_invalid_primitive_root(self):
        prime = 11  # Known small prime
        root = find_primitive_root(prime)
        self.assertNotEqual(pow(root, prime-1, prime), 1, "Invalid primitive root detected.")

    def test_invalid_key_generation(self):
        p = 23  # Small prime for testing
        g = find_primitive_root(p)
        private_key, public_key = generate_elgamal_keys(p, g)
        self.assertNotEqual(private_key, 0, "Private key should not be 0.")
        self.assertNotEqual(private_key, p-1, "Private key should not be p-1.")

    def test_encryption_with_special_characters(self):
        p = generate_large_prime(256)
        g = find_primitive_root(p)
        private_key, public_key = generate_elgamal_keys(p, g)
        original_message = 'Hello!@#$'
        # Assuming the encryption function can handle non-numeric messages
        c1, c2 = elgamal_encrypt(public_key, p, g, original_message)
        decrypted_message = elgamal_decrypt(private_key, p, c1, c2)
        self.assertEqual(original_message, decrypted_message, "Special character handling failed in encryption/decryption.")

    def test_decryption_with_wrong_key(self):
        p = generate_large_prime(256)
        g = find_primitive_root(p)
        _, public_key = generate_elgamal_keys(p, g)
        private_key = 123456  # Random wrong private key
        original_message = '1234567890'
        c1, c2 = elgamal_encrypt(public_key, p, g, original_message)
        decrypted_message = elgamal_decrypt(private_key, p, c1, c2)
        self.assertNotEqual(original_message, decrypted_message, "Decryption should fail with wrong private key.")

if __name__ == '__main__':
    unittest.main()
