# main.py
import gnupg
from io import BytesIO
from encrypt import encrypt_file
from decrypt import decrypt_file

def main():
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'

    # Generate key pair (if you don't have keys already)
    input_data = gpg.gen_key_input(
        name_email='msabdulkarimcpt@gmail.com',
        passphrase='12345'
    )

    key = gpg.gen_key(input_data)

    # Export public and private keys
    public_key = gpg.export_keys(key.fingerprint)
    private_key = gpg.export_keys(key.fingerprint, secret=True, passphrase='12345')

    # Save keys to files (optional)
    with open('public_key.asc', 'w') as file:
        file.write(public_key)

    with open('private_key.asc', 'w') as file:
        file.write(private_key)
    
    with open('data.txt', 'r') as file:
        file_content = file.read()

    key_in_bytes = BytesIO(public_key.encode('utf-8'))
    file_content_in_bytes = BytesIO(file_content.encode('utf-8'))

    # Encrypt the file
    encrypted_file = encrypt_file(key_in_bytes, file_content_in_bytes)
    
    encrypted_content = encrypted_file.getvalue()
    
    print("Encrypted content:", encrypted_content)
    
    # Reset the key and file for decryption
    key = BytesIO(private_key.encode('utf-8'))
    file = BytesIO(encrypted_content)
    
    # Decrypt the file
    decrypted_file = decrypt_file(key, file)
    decrypted_content = decrypted_file.getvalue().decode('utf-8')
    
    print("Decrypted content:", decrypted_content)

if __name__ == "__main__":
    main()
