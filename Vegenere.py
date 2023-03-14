# rilew fretj qgzrv uperr vdajq grwue qrszh clcer nqjlc dstqv aluan ouedm qbqgr mhwqh etgqz yh
# ainsi sontl esmoe ursde smale setde sfeme llesd ansle regne anima ldefa conpr ovide ntiel le

def encrypt(text, key) :

	encrypted = ""
	j = 0

	for i in range(len(text)) :

		if text[i] == " " :
			encrypted = encrypted + " "
		else :
			encrypted += chr((ord(text[i]) + ord(key[j]) - 168) % 26 + 97)
			j = (j+1) % len(key)

	return encrypted

def decrypt(cipher, key) :
  
  decrypted = ""
  j = 0

  for i in range(len(cipher)) :

    if cipher[i] == " " :
      decrypted = decrypted + " "
    else :
      decrypted += chr((ord(cipher[i]) - ord(key[j]) + 26) % 26 + 97)
      j = (j+1) % len(key)
  
  return decrypted

text = input("Enter a text: ")
key = input("key: ")

print("\n-------------------------")
print("Ciphertext: " + decrypt(text, key))
print("-------------------------")