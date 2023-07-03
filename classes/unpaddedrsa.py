class UnpaddedRSA:
    def __init__(self, p, q, n, e=65537):
        self.p = p
        self.q = q
        self.n = n
        self.phi = (p - 1) * (q - 1)
        self.e = e
        self.d = pow(self.e, -1, self.phi)

    def encrypt(self, message):
        ciphertext = pow(message, self.e, self.n)
        return ciphertext

    def decrypt(self, ciphertext):
        message = pow(ciphertext, self.d, self.n)
        return message

    def multiply(self, ciphertext1, ciphertext2):
        ciphertext_new = (ciphertext1 * ciphertext2) % self.n
        return ciphertext_new

    def verify_homomorphic_property(self, message1, message2, result):
        decrypted_result = self.decrypt(result)
        expected_result = (message1 * message2) % self.n

        return decrypted_result == expected_result