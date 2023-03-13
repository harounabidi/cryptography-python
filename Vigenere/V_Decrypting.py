# rilew fretj qgzrv uperr vdajq grwue qrszh clcer nqjlc dstqv aluan ouedm qbqgr mhwqh etgqz yh

def vigenere_decrypt(cipher, key) :
  
  spaces_indexes = []
  
  # put space indexes in array
  for i in range(len(cipher)) :
    if cipher[i] == " " :
      spaces_indexes.append(i)
  
  decrypted = ""
  
  # remove spaces from the cipher
  cipher_ws = cipher.replace(" ", "")

  # decrypt cipher without spaces
  for i in range(len(cipher_ws)) :

    cipher_p = ord(cipher_ws[i])
    key_p = ord(key[i % len(key)])
    
    decrypted += chr((cipher_p - key_p + 26) % 26 + 97)

  # check if i is in space indexes array and add a space to encrypted text 
  for i in spaces_indexes :
    decrypted = decrypted[:i] + " " + decrypted[i:]
  
  return decrypted

# cipher = input("Enter a cipher to decrypt: ")
cipher = "rilew fretj qgzrv uperr vdajq grwue qrszh clcer nqjlc dstqv aluan ouedm qbqgr mhwqh etgqz yh"

# key = input("Decryption key: ")
key = "raymond"

print("\n-------------------------")
print("Plaintext: " + vigenere_decrypt(cipher, key))
print("-------------------------")