import random

class ElGamal:
    def __init__(self, p):
        self.p = p
        self.g = random.randint(1, p - 1)

        # Generate private key
        self.private_key = random.randint(1, p - 1)

        # Compute public key
        self.public_key = pow(self.g, self.private_key, p)
            
    def encrypt(self, message):
        # Generate random ephemeral key
        k = random.randint(1, self.p - 1)

        # Compute the shared secret
        s = pow(self.public_key, k, self.p)

        # Compute the ciphertext components
        c1 = pow(self.g, k, self.p)
        c2 = (message * s) % self.p

        return c1, c2

    def decrypt(self, ciphertext):
        c1, c2 = ciphertext

        # Compute the shared secret
        s = pow(c1, self.private_key, self.p)

        # Compute the plaintext by dividing c2 by the shared secret
        message = (c2 * pow(s, self.p - 2, self.p)) % self.p

        return message

    def multiply(self, ciphertext1, ciphertext2):
        c1_new = (ciphertext1[0] * ciphertext2[0]) % self.p
        c2_new = (ciphertext1[1] * ciphertext2[1]) % self.p
        return c1_new, c2_new

    def verify_homomorphic_property(self, message1, message2, result):
        decrypted_result = self.decrypt(result)
        expected_result = (message1 * message2) % self.p

        return decrypted_result == expected_result
