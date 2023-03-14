import rsa

# A create a private and a public key pair
(a_public, a_private) = rsa.newkeys(512)

# A gives the public key to B


# B writes a message
s_message = 'Hello World'.encode('utf8')

# B encrypts the message with A public key

crypto = rsa.encrypt(s_message, a_public)

# A receives the encrypted message

r_message = rsa.decrypt(crypto, a_private)


# A decrypt the message with its private key

print(r_message.decode('utf8'))