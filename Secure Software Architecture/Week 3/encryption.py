from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt data
plain_text = b"I think, therefore I am."
cipher_text = cipher_suite.encrypt(plain_text)
print("Encrypted:", cipher_text)

# Decrypt data
decrypted_text = cipher_suite.decrypt(cipher_text)
print("Decrypted:", decrypted_text)