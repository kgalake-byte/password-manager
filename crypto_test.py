from cryptography.fernet import Fernet

def main():
    print("Testing Fernet:")
    key = Fernet.generate_key()
    print(f"Key: {key.decode()}")
    
    cipher = Fernet(key)
    test_str = "Hello World".encode()
    encrypted = cipher.encrypt(test_str)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Original: {test_str.decode()}")
    print(f"Decrypted: {decrypted.decode()}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
