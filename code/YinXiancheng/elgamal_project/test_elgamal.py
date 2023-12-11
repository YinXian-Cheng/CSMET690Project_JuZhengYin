import unittest
from sympy import isprime
from elgamal_key_generation_by_bob import generate_keys
from elgamal_encryption import encrypt_message
from elgamal_decryption import decrypt_message


class TestElGamal(unittest.TestCase):

    def test_key_generation(self):
        p, g, B, b = generate_keys()
        self.assertIsInstance(p, int, "p should be an integer")
        self.assertIsInstance(g, int, "g should be an integer")
        self.assertIsInstance(B, int, "B should be an integer")
        self.assertIsInstance(b, int, "b should be an integer")

        self.assertTrue(isprime(p), "p should be a prime number")
        self.assertLess(g, p, "g should be less than p")
        self.assertGreater(b, 1, "b should be greater than 1")
        self.assertLess(b, p, "b should be less than p")

        expected_B = pow(g, b, p)
        self.assertEqual(B, expected_B, "B should be equal to g^b mod p")

    def test_encryption_and_decryption(self):
        p, g, B, b = generate_keys()
        public_key = (p, g, B)
        private_key = b

        original_message = 123456789
        encrypted_message = encrypt_message(original_message, public_key)
        decrypted_message = decrypt_message(encrypted_message, private_key, p)

        self.assertEqual(original_message, decrypted_message)

    def test_encryption_with_various_messages(self):
        p, g, B, b = generate_keys()
        public_key = (p, g, B)
        private_key = b

        for message in [0, 1, 2, p-1, 123456789]:
            with self.subTest(message=message):
                encrypted_message = encrypt_message(message, public_key)
                decrypted_message = decrypt_message(encrypted_message, private_key, p)
                self.assertEqual(message, decrypted_message, f"Decryption failed for message: {message}")

    def test_decryption_with_incorrect_key(self):
        p, g, B, b = generate_keys()
        public_key = (p, g, B)
        incorrect_private_key = b + 1  # intentionally incorrect key

        original_message = 123
        encrypted_message = encrypt_message(original_message, public_key)
        decrypted_message = decrypt_message(encrypted_message, incorrect_private_key, p)

        self.assertNotEqual(original_message, decrypted_message, "Decryption with incorrect key should not return original message")

    def test_invalid_inputs(self):
        p, g, B, b = generate_keys()
        public_key = (p, g, B)

        with self.assertRaises(ValueError):
            encrypt_message("not an integer", public_key)

        with self.assertRaises(ValueError):
            encrypt_message(-1, public_key)

    def test_private_key_boundaries(self):
        p, g, B, b = generate_keys()

        for b_test in [1, p - 1]:
            with self.subTest(b=b_test):
                B_test = pow(g, b_test, p)
                encrypted_message = encrypt_message(123, (p, g, B_test))
                decrypted_message = decrypt_message(encrypted_message, b_test, p)
                self.assertEqual(123, decrypted_message, f"Failed at boundary b={b_test}")


if __name__ == '__main__':
    unittest.main()
