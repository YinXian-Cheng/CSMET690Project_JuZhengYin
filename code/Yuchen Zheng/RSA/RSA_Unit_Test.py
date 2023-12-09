# RSA_Unit_Test.py

import unittest
from RSA_Generates_Public_And_Private_Keys import generate_keys, is_prime, generate_prime_number
from RSA_Generates_Encrypted_Information import rsa_encrypt
from RSA_Generates_Decryption_Information import rsa_decrypt
from RSA_Generate_Hacker import attempt_prime_factorization

class TestRSAEncryption(unittest.TestCase):

    def test_prime_generation(self):
        _, _, n = generate_keys()
        self.assertTrue(is_prime(n), "Generated number is not a prime.")

    def test_rsa_key_generation(self):
        public_key, private_key, _ = generate_keys()
        self.assertIsInstance(public_key, int, "Public key is not an integer.")
        self.assertIsInstance(private_key, int, "Private key is not an integer.")

    def test_rsa_encryption_decryption(self):
        public_key, private_key, n = generate_keys()
        original_message = "Test message"
        encrypted_message = rsa_encrypt(public_key, n, original_message)
        decrypted_message = rsa_decrypt(private_key, n, encrypted_message)
        self.assertEqual(original_message, decrypted_message, "Decrypted message does not match the original.")

    def test_rsa_hacker_module(self):
        _, _, n = generate_keys()
        factors = attempt_prime_factorization(n, time_limit=5)
        if factors:
            self.assertEqual(n, factors[0] * factors[1], "Failed to correctly factorize the modulus.")
        else:
            self.assertIsNone(factors, "Factorization should either return None or the correct factors.")

    def test_small_prime_generation(self):
        small_prime = generate_prime_number(32)
        self.assertTrue(is_prime(small_prime), "Failed to generate a small prime.")

    def test_known_primes(self):
        known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in known_primes:
            self.assertTrue(is_prime(prime), f"{prime} should be identified as a prime.")

    def test_known_non_primes(self):
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), f"{non_prime} should be identified as a non-prime.")

    def test_rsa_encryption_with_special_characters(self):
        public_key, private_key, n = generate_keys()
        original_message = "Special characters: !@#$%^&*()"
        encrypted_message = rsa_encrypt(public_key, n, original_message)
        decrypted_message = rsa_decrypt(private_key, n, encrypted_message)
        self.assertEqual(original_message, decrypted_message, "Failed to encrypt/decrypt message with special characters.")

    def test_rsa_decryption_with_wrong_key(self):
        public_key, _, n = generate_keys()
        wrong_private_key = 123456789  # Arbitrary wrong private key
        original_message = "Test message"
        encrypted_message = rsa_encrypt(public_key, n, original_message)
        with self.assertRaises(Exception):
            rsa_decrypt(wrong_private_key, n, encrypted_message)

if __name__ == '__main__':
    unittest.main()

