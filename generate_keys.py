import os
import json
from Crypto.Util.number import getPrime

# Key size
key_lengths = [512, 1024, 2048]

rsa_keys = {}
# RSA key generator
for key_length in key_lengths:
    bit_count = 0
    while bit_count != key_length:
        # Generate prime numbers
        p = getPrime(key_length // 2)
        q = getPrime(key_length // 2)

        n = p*q
        bit_count = n.bit_length()

    rsa_keys[str(key_length)] = {'p': p, 'q': q, 'n': n}

elgamal_keys = {}
# ElGamal key generator
for key_length in key_lengths:
    p = getPrime(key_length)
    elgamal_keys[str(key_length)] = {'p': p}

rsa_path = './keys/rsa.json'
elgamal_path = './keys/elgamal.json'

# Check if the files exist and remove them if necessary
if os.path.exists(rsa_path):
    os.remove(rsa_path)
if os.path.exists(elgamal_path):
    os.remove(elgamal_path)

# Dump rsa_keys to JSON file
with open(rsa_path, "w") as rsa_file:
    json.dump(rsa_keys, rsa_file)

# Dump elgamal_keys to JSON file
with open(elgamal_path, "w") as elgamal_file:
    json.dump(elgamal_keys, elgamal_file)
