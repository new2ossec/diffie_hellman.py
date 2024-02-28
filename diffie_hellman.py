import random

import Crypto.Util.number as cun
from Crypto.Cipher import AES

rand = random.SystemRandom()

class Person():
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self._a = rand.randrange(2, self.p - 1)
        self.A = pow(self.g, self._a, self.p)

    def publicKey(self):
        return self.A
    
    def createSharedSecret(self, public_key):
        self._sharedsecret = pow(public_key, self._a, p)

    def checkkey(self):
        return self._sharedsecret
    
print("Parameter known by Alice and Bob")
#Generate random prime p
p = cun.getPrime(512)

#Choose a generator
g = 5
print(f"p = {p}")
print(f"g = {g}")


alice = Person(p, g)
A = alice.publicKey()
print(f"Alice public key: {A}")

bob = Person(p,g)
B = bob.publicKey()
print(f"Bob public key: {B}")

# Alice and Bob create their shared secrets with the public key of the other one
alice.createSharedSecret(B)
bob.createSharedSecret(A)

secretFromAlice = alice.checkkey()
secretFromBob = bob.checkkey()

print(f"Alice shared secret: {secretFromAlice}")
print(f"Bob shared secret: {secretFromBob}")

if secretFromBob == secretFromAlice:
    print("Keys exchanged perfectly")
else:
    print("There was an issue during the exchange")
