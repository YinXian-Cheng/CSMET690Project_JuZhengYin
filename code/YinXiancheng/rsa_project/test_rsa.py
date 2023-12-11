import unittest
from rsa_key_generation import generate_rsa_keys
from rsa_encryption import encrypt_message_rsa
from rsa_decryption import decrypt_message_rsa


class TestRSA(unittest.TestCase):

    def test_key_generation(self):
        public_key, private_key = generate_rsa_keys()
        e, n = public_key
        d, n_private = private_key

        self.assertIsInstance(e, int, "e should be an integer")
        self.assertIsInstance(d, int, "d should be an integer")
        self.assertEqual(n, n_private, "n should be the same in both public and private keys")

    def test_encryption_and_decryption(self):
        public_key, private_key = generate_rsa_keys()

        original_message = 1357924680
        encrypted_message = encrypt_message_rsa(original_message, public_key)
        decrypted_message = decrypt_message_rsa(encrypted_message, private_key)

        self.assertEqual(original_message, decrypted_message, "Decryption failed")

    def test_encryption_with_various_messages(self):
        public_key, private_key = generate_rsa_keys()

        for message in [0, 1, 10086, 1357924680]:
            with self.subTest(message=message):
                encrypted_message = encrypt_message_rsa(message, public_key)
                decrypted_message = decrypt_message_rsa(encrypted_message, private_key)
                self.assertEqual(message, decrypted_message, f"Decryption failed for message: {message}")

    def test_invalid_inputs(self):
        public_key, _ = generate_rsa_keys()

        with self.assertRaises(ValueError):
            encrypt_message_rsa("not an integer", public_key)

        with self.assertRaises(ValueError):
            encrypt_message_rsa(-1, public_key)


if __name__ == '__main__':
    unittest.main()
