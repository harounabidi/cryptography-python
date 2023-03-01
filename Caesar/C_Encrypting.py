def caesar_encrypt(text, key) :

	encrypted = ""
	
	for i in range(len(text)) :
		
		text_p = ord(text[i]) - 97
		key_p = ord(key) - 97

		if text[i] == " " :
			encrypted += " "
		else :
			encrypted += chr((text_p + key_p) % 26 + 97)

	return encrypted

text = input("Enter a text to encrypt: ")
key = input("Encryption key: ")

print("\n-------------------------")
print("Ciphertext: " + caesar_encrypt(text, key))
print("-------------------------")