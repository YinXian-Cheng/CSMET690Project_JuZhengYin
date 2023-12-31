I.File functions:

ElGamal_Generate_Primes_And_Primitive_Roots.py:

Function: Generate large prime number p and primitive root g.
Role interaction: These values are generated and exposed by the initiator of the cryptographic system (which may be Alice or an independent trusted entity).

ElGamal_Generate_Private_and_Public_Keys.py:

Function: Generate private key and public key.
Role interaction: The private key is kept secret by its owner (Bob), while the public key is made public and can be used by other roles (such as Alice and Eve).

ElGamal_Generate_Encrypted_Information.py:

Function: Use the public key to encrypt information.
Role interaction: Alice uses Bob's public key to encrypt the message, and the resulting encrypted message can be received by Bob (and potentially Eve).

ElGamal_Generate_Decrypted_Information.py:

Function: Use the private key to decrypt information.
Role interaction: Bob uses his private key to decrypt the encrypted message sent by Alice. If Eve tries to decrypt the message, she cannot succeed unless she can find Bob's private key.

ElGamal_Generate_Hacker.py:

Function: Try to crack the encrypted information.
Character Interaction: Eve uses this script to attempt to decrypt Alice's message by brute-forcing Bob's private key.

ElGamal_number_and_root.txt:

Function: Contains information about large prime numbers p and primitive roots g.
Role interaction: This information is public and provided to all participants by the initiator of the cryptographic system.

ElGamal_private_and_public_keys.txt:

Function: Contains private key and public key information.
Role interaction: The public key is public and can be used by all participants, while the private key must be kept secret and known only to its owner.

ElGamal_encrypted_Information.txt and ElGamal_decryption_Information.txt:

Function: Contains encrypted and decrypted information respectively.
Role interaction: The encrypted information (ElGamal_encrypted_Information.txt) is generated by Alice and sent to Bob (Eve may also intercept it), while the decrypted information (ElGamal_decryption_Information.txt) is obtained by Bob using his own private key and should not be known to Eve in theory. .

II.Usage process:

1. ElGamal_Generate_Primes_And_Primitive_Roots.py:

First run this script to generate a large prime number p and a primitive root g. These parameters are the basis of the entire encryption system.
The results can be saved in "ElGamal_number_and_root.txt" for subsequent use.

2. ElGamal_Generate_Private_and_Public_Keys.py:

Use the p and g generated in the first step to generate the private and public keys.
The public key will be made public (for example, Alice can make her public key public), while the private key must be kept secret (known only to Alice).
Information about private and public keys can be saved in "ElGamal_private_and_public_keys.txt".

3. ElGamal_Generate_Encrypted_Information.py:

Alice encrypts her message using Bob's public key (obtained from step 2).
Encrypted messages can be saved in "ElGamal_encrypted_Information.txt".

4. ElGamal_Generate_Decrypted_Information.py:

Bob uses his private key (obtained from step 2) to decrypt Alice's message.
The decrypted message can be saved in "ElGamal_decryption_Information.txt".

5. ElGamal_Generate_Hacker.py:

This script simulates a hacker (Eve) trying to crack an encrypted message.
It tries to find Bob's private key and use it to decrypt Alice's message.
This step is used to demonstrate the security of the ElGamal encryption system and is usually not part of the normal encryption and decryption process.

III.Test method

Run ElGamal_Unit_Test.py to perform unit testing.
