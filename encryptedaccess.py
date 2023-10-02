from cryptography.fernet import Fernet

# Generate a key and save it securely
key = Fernet.generate_key()

# Initialize the encryption
cipher_suite = Fernet(key)

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()

# Usage:
encrypted_api_key = encrypt_message("YOUR_BINANCE_API_KEY")
decrypted_api_key = decrypt_message(encrypted_api_key)
