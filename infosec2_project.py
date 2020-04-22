from Crypto.PublicKey import RSA
from hashlib import sha512


#key length of 2048, claimed to be sufficient until the year 2030
keyPair = RSA.generate(bits=2048)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print()
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

print("\n\n")

msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)

# RSA verify signature (tampered msg)
msg = b'A message for signing (tampered)'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid (tampered):", hash == hashFromSignature)
'''
import numpy as np
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
private_key = rsa.generate_private_key(
     public_exponent=65537, key_size=2048, backend=default_backend()
... )

# Sign a message using the key
message = b"A message I want to sign"
signature = private_key.sign(
...     message, 
...     padding.PSS(
...         mgf=padding.MGF1(hashes.SHA256()),
...         salt_length=padding.PSS.MAX_LENGTH
...     ),
...     hashes.SHA256()
... )


def digital_sign( str ):
   "This prints a passed string into this function"
   print(str)
   return;


def main():
    digital_sign()


if __name__ == "__main__":
    main()


'''