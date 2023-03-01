# ciphertext: rilew fretj qgzrv uperr vdajq grwue qrwue qrszh clcer nqjlc dstqv aluan ouedm qbqgr mhwqh etgqz yh
# key: raymond

def vigenere_decrypt(text, key) :
    
  decrypted = ""

  for i in range(len(text)) :

    text_p = ord(text[i])
    key_p = ord(key[i % len(key)])
    
    if text[i] == " " :
      decrypted += " "
    else :
      decrypted += chr((text_p - key_p) % 26 + 97)

  return decrypted

text = input("Enter a text to decrypt: ")
key = input("Decryption key: ")

print("\n-------------------------")
print("Plaintext: " + vigenere_decrypt(text, key))
print("-------------------------")