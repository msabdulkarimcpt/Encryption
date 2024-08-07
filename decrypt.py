import gnupg
from typing import IO
from io import BytesIO

def decrypt_file(key: IO, file: IO, passphrase: str = None) -> IO:
    gpg = gnupg.GPG()
    
    # Import the private key
    key_data = key.read()
    import_result = gpg.import_keys(key_data)
    
    if not import_result.count:
        raise ValueError("Failed to import the PGP key")
    
    # Decrypt the file
    if passphrase:
        decrypted_data = gpg.decrypt_file(file, passphrase=passphrase)
    else:
        decrypted_data = gpg.decrypt_file(file)
    
    if not decrypted_data.ok:
        raise ValueError(f"Decryption failed: {decrypted_data.status}")
    
    # Create an in-memory file for the decrypted data
    decrypted_file = BytesIO(decrypted_data.data)
    
    return decrypted_file
