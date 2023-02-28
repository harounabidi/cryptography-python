def encrypt(text, c) :

	crypted = ""

	for i in range(len(text)) :

		if text[i] == " " :
			crypted += " "
		else :
			crypted += chr((ord(text[i]) + ord(c) - 194)%26 + 97)

	return crypted

text = input("Enter a text to encrypt: ")
c = input("Encryption key: ")

print("\n-------------------------")
print("Ciphertext: " + encrypt(text, c))
print("-------------------------")