# ciphertext: tv kvokv r vkv tyzwwiv rmvt ar tav h
# key: r

def caesar_decrypt(text, key) :
	
	decrypted = ""

	for i in range(len(text)) :

		text_p = ord(text[i])
		key_p = ord(key)

		if text[i] == " " :
			decrypted += " "
		else :
			decrypted += chr((text_p - key_p) % 26 + 97)
	
	return decrypted

text = input("Enter a text to decrypt: ")
key = input("Decryption key: ")

print("\n-------------------------")
print("Plaintext: " + caesar_decrypt(text, key))
print("-------------------------")