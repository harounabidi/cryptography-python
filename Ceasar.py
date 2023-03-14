# ciphertext: tv kvokv r vkv tyzwwiv rmvt ar tav h
# key: r

def decrypt(text, key) :
	
	decrypted = ""

	for i in range(len(text)) :

		text_p = ord(text[i])
		key_p = ord(key)

		if text[i] == " " :
			decrypted += " "
		else :
			decrypted += chr((text_p - key_p) % 26 + 97)
	
	return decrypted

def encrypt(text, key) :

	encrypted = ""
	
	for i in range(len(text)) :
		
		text_p = ord(text[i]) - 97
		key_p = ord(key) - 97

		if text[i] == " " :
			encrypted += " "
		else :
			encrypted += chr((text_p + key_p) % 26 + 97)

	return encrypted

text = input("Enter a text: ")
key = input("key: ")

print("\n-------------------------")
print("Plaintext: " + decrypt(text, key))
print("-------------------------")