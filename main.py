# main.py
import gnupg
from io import BytesIO
from encrypt import encrypt_file
from decrypt import decrypt_file
from typing import Any

def generate_key_pair(gpg: Any, email: str, passphrase: str) -> str:
    input_data = gpg.gen_key_input(
        name_email=email,
        passphrase=passphrase
    )
    key = gpg.gen_key(input_data)
    return key.fingerprint

def export_public_key(email: str, passphrase: str) -> str:
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    fingerprint = generate_key_pair(gpg, email, passphrase)
    return gpg.export_keys(fingerprint)

def export_private_key(email: str, passphrase: str) -> str:
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    fingerprint = generate_key_pair(gpg, email, passphrase)
    return gpg.export_keys(fingerprint, secret=True, passphrase=passphrase)

def main():
    email = 'abc@abc.com'
    passphrase = '12345'

    # gpg = gnupg.GPG()
    # gpg.encoding = 'utf-8'

    # Export public and private keys
    public_key = export_public_key(email, passphrase)
    private_key = export_private_key(email, passphrase)

    # Save keys to files (optional)
    with open('public_key.asc', 'w') as file:
        file.write(public_key)

    with open('private_key.asc', 'w') as file:
        file.write(private_key)
    
    with open('data.txt', 'r') as file:
        file_content = file.read()

    print("File content:", file_content)

    key_in_bytes = BytesIO(public_key.encode('utf-8'))
    file_content_in_bytes = BytesIO(file_content.encode('utf-8'))

    # Encrypt the file
    encrypted_file = encrypt_file(key_in_bytes, file_content_in_bytes)
    
    encrypted_content = encrypted_file.getvalue()
    
    #print("Encrypted content:", encrypted_content)
    
    # Reset the key and file for decryption
    key = BytesIO(private_key.encode('utf-8'))
    file = BytesIO(encrypted_content)
    
    # Decrypt the file
    decrypted_file = decrypt_file(key, file, passphrase)
    decrypted_content = decrypted_file.getvalue().decode('utf-8')
    
    print("Decrypted content:", decrypted_content)

if __name__ == "__main__":
    main()
