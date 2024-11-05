# A python program to illustrate Caesar Cipher Technique

to_encrypt = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))


def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + s) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)

        # Symbols and non-text characters
        else:
            result += char

    return result


def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 - s) % 26 + 65)

        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 - s) % 26 + 97)

        # Symbols and non-text characters
        else:
            result += char

    return result


print("Text  : " + to_encrypt)
print("Shift : " + str(shift))
print("Cipher: " + encrypt(to_encrypt, shift))

to_decrypt = input("Enter the text to decrypt: ")
decrypt_shift = int(input("Enter the shift value for decryption: "))

print("Decrypted: " + decrypt(to_decrypt, decrypt_shift))
