# Cipher algorithm with python

## Encryption function

`ord(text[i])` is the position of the character in our ciphertext.

`ord(c)` is the position of the encryption key character in accii table.

`% 26` is used to circulate through the 26 alphabets (from 0 to 25), we added 97 because the first character (small case a) in ASCII code is 97.

```python
encrypted += chr((text_p + key_p) % 26 + 97)
```

## Decryption function

Is the same as the encryption function but instead of shifting the characters to the right, we shift them to the left (substracting the position of the decryption key).

```python
encrypted += chr((text_p - key_p) % 26 + 97)
```
