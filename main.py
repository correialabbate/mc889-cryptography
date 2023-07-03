import json
import random
from classes.unpaddedrsa import UnpaddedRSA
from classes.elgamal import ElGamal
import time

def read_keys():
    rsa_path = './keys/rsa.json'
    elgamal_path = './keys/elgamal.json'

    # Read rsa_keys from JSON file
    with open(rsa_path, "r") as rsa_file:
        rsa_keys = json.load(rsa_file)

    # Read elgamal_keys from JSON file
    with open(elgamal_path, "r") as elgamal_file:
        elgamal_keys = json.load(elgamal_file)

    return rsa_keys, elgamal_keys

# Read keys generated by the generate_keys.py script
rsa_keys, elgamal_keys = read_keys()

# RSA and ElGamal execution
for key in rsa_keys:
    print('Key size: ' + key)
    p = rsa_keys[key]['p']
    q = rsa_keys[key]['q']
    n = rsa_keys[key]['n']
    unpadded_rsa = UnpaddedRSA(p=p, q=q, n=n)

    # Generate random messages, same messages for RSA and ElGamal
    message1 = random.randint(1, n - 1)
    print('Mensagem 1, bit lenght: ' + str(message1.bit_length()))
    message2 = random.randint(1, n - 1)
    print('Mensagem 2, bit lenght: ' + str(message1.bit_length()))

    rsa_total_encrypt_m1 = 0
    rsa_total_encrypt_m2 = 0
    eg_total_encrypt_m1 = 0
    eg_total_encrypt_m2 = 0
    rsa_total_multiply = 0
    eg_total_multiply = 0
    rsa_total_decrypt = 0
    eg_total_decrypt = 0

    for i in range(100):
        # Encrypt messages
        start = time.process_time()
        ciphertext1 = unpadded_rsa.encrypt(message1)
        rsa_time_encrypt_ciphertext1 = (time.process_time() - start)
        start = time.process_time()
        ciphertext2 = unpadded_rsa.encrypt(message2)
        rsa_time_encrypt_ciphertext2 = (time.process_time() - start)

        # Multiply the encrypted ciphertexts
        start = time.process_time()
        ciphertext3 = unpadded_rsa.multiply(ciphertext1, ciphertext2)
        rsa_time_multiply = (time.process_time() - start)

        start = time.process_time()
        decrypted_value = unpadded_rsa.decrypt(ciphertext3)
        rsa_time_decrypt_ciphertext3 = (time.process_time() - start)

        verify_property = unpadded_rsa.verify_homomorphic_property(message1=message1, message2=message2, result=ciphertext3)
        # if verify_property:
        #     print('RSA homomorphic property WORKED for key lenght ' + key)
        # else:
        #     print('RSA homomorphic property DID NOT WORK for key lenght ' + key)

        # ElGamal execution
        p = elgamal_keys[key]['p']
        elgamal = ElGamal(p=p)

        # Encrypt messages
        start = time.process_time()
        ciphertext1 = elgamal.encrypt(message1)
        eg_time_encrypt_ciphertext1 = (time.process_time() - start)
        start = time.process_time()
        ciphertext2 = elgamal.encrypt(message2)
        eg_time_encrypt_ciphertext2 = (time.process_time() - start)

        # Multiply the encrypted ciphertexts
        start = time.process_time()
        ciphertext3 = elgamal.multiply(ciphertext1, ciphertext2)
        eg_time_multiply = (time.process_time() - start)

        start = time.process_time()
        decrypted_value = elgamal.decrypt(ciphertext3)
        eg_time_decrypt_ciphertext3 = (time.process_time() - start)

        verify_property = elgamal.verify_homomorphic_property(message1=message1, message2=message2, result=ciphertext3)
        # if verify_property:
        #     print('ElGamal homomorphic property WORKED for key lenght ' + key)
        # else:
        #     print('ElGamal homomorphic property DID NOT WORK for key lenght ' + key)

        rsa_total_encrypt_m1 += rsa_time_encrypt_ciphertext1
        rsa_total_encrypt_m2 += rsa_time_encrypt_ciphertext2
        eg_total_encrypt_m1 += eg_time_encrypt_ciphertext1
        eg_total_encrypt_m2 += eg_time_encrypt_ciphertext2
        rsa_total_multiply += rsa_time_multiply
        eg_total_multiply += eg_time_multiply
        rsa_total_decrypt += rsa_time_decrypt_ciphertext3
        eg_total_decrypt += eg_time_decrypt_ciphertext3
        
    rsa_avg_encrypt_m1 = rsa_total_encrypt_m1/100
    rsa_avg_encrypt_m2 = rsa_total_encrypt_m2/100
    rsa_avg_multiply = rsa_total_multiply/100
    rsa_avg_decrypt = rsa_total_decrypt/100

    eg_avg_encrypt_m1 = eg_total_encrypt_m1/100
    eg_avg_encrypt_m2 = eg_total_encrypt_m2/100
    eg_avg_multiply = eg_total_multiply/100
    eg_avg_decrypt = eg_total_decrypt/100

    print('rsa_avg_encrypt_m1: ' + str(rsa_avg_encrypt_m1))
    print('rsa_avg_encrypt_m2: '+ str(rsa_avg_encrypt_m2))
    print('rsa_avg_multiply: '+ str(rsa_avg_multiply))
    print('rsa_avg_decrypt: '+ str(rsa_avg_decrypt))
    print('rsa_avg_encrypt: ' + str((rsa_avg_encrypt_m1 + rsa_avg_encrypt_m2)/2))

    print('eg_avg_encrypt_m1: ' + str(eg_avg_encrypt_m1))
    print('eg_avg_encrypt_m2: ' + str(eg_avg_encrypt_m2))
    print('eg_avg_multiply: ' + str(eg_avg_multiply))
    print('eg_avg_decrypt: ' + str(eg_avg_decrypt))
    print('eg_avg_encrypt: ' + str((eg_avg_encrypt_m1 + eg_avg_encrypt_m2)/2))

