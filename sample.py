import gnupg

# Initialize GPG
gpg = gnupg.GPG(gnupghome='C:\\Users\\msabd\\MyGnuPG')
gpg.encoding = 'utf-8'

 # Generate key pair (if you don't have keys already)
input_data = gpg.gen_key_input(
    name_email='msabdulkarimcpt@gmail.com',
    passphrase='12345'
)

key = gpg.gen_key(input_data)

# Export public and private keys
public_key = gpg.export_keys(key.fingerprint)
private_key = gpg.export_keys(key.fingerprint, secret=True, passphrase='101')

# Save keys to files (optional)
with open('public_key.asc', 'w') as f:
    f.write(public_key)

with open('private_key.asc', 'w') as f:
    f.write(private_key)

# Encrypt a file
with open('data.txt', 'rb') as f:
    status = gpg.encrypt_file(
        f, recipients=['msabdulkarimcpt@gmail.com'],
        output='data.txt.gpg'
    )

if status.ok:
    print('File encrypted successfully')
else:
    print('Encryption failed:', status.status)

# Decrypt the file
with open('data.txt.gpg', 'rb') as f:
    status = gpg.decrypt_file(f, passphrase='101', output='decrypted_file.txt')

if status.ok:
    print('File decrypted successfully')
else:
    print('Decryption failed:', status.status)
