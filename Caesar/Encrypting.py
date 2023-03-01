def caesar_encrypt(text, c) :

	encrypted = ""

	for i in range(len(text)) :

		if text[i] == " " :
			encrypted += " "
		else :
			encrypted += chr((ord(text[i]) + ord(c) - 194) % 26 + 97)

	return encrypted

text = input("Enter a text to encrypt: ")
c = input("Encryption key: ")

print("\n-------------------------")
print("Ciphertext: " + caesar_encrypt(text, c))
print("-------------------------")