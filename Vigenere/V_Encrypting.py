def vigenere_encrypt(text, key) :

	spaces_indexes = []

  # put space indexes in array
	for i in range(len(text)):
		if text[i] == " ":
			spaces_indexes.append(i)

	encrypted = ""
	
	# remove spaces from the text
	text_ws = text.replace(" ", "")

  # encrypt text without spaces
	for i in range(len(text_ws)) :
		
		text_p = ord(text_ws[i]) - 97
		key_p = ord(key[i % len(key)]) - 97

		encrypted += chr((text_p + key_p) % 26 + 97)

	
	# check if i is in space indexes array and add a space to encrypted text
	for i in spaces_indexes :
		encrypted = encrypted[:i] + " " + encrypted[i:]

	return encrypted

# text = input("Enter a text to encrypt: ")
text = "ainsi sontl esmoe ursde smale setde sfeme llesd ansle regne anima ldefa conpr ovide ntiel le"

# key = input("Encryption key: ")
key = "raymond"

print("\n-------------------------")
print("Ciphertext: " + vigenere_encrypt(text, key))
print("-------------------------")