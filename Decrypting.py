def decrypt(text, c) :

	decrypted = ""

	for i in range(len(text)) :

		if text[i] == " " :
			decrypted += " "
		else :
			decrypted += chr((ord(text[i]) - ord(c)) % 26 + 97)

	return decrypted

text = input("Enter a text to decrypt: ")
c = input("Decryption key: ")

print("\n-------------------------")
print("Plaintext: " + decrypt(text, c))
print("-------------------------")