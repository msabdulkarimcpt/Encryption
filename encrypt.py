import gnupg
from typing import IO
from io import BytesIO

def encrypt_file(key: IO, file: IO) -> IO:
    gpg = gnupg.GPG()
  
    # Import the key
    key_data = key.read()
    import_result = gpg.import_keys(key_data)
    
    if not import_result.count:
        raise ValueError("Failed to import the PGP key")
    
    # Encrypt the file
    encrypted_data = gpg.encrypt_file(file, recipients=[import_result.fingerprints[0]], always_trust=True, output=None)
    
    if not encrypted_data.ok:
        raise ValueError(f"Encryption failed: {encrypted_data.status}")
    
    # Create an in-memory file for the encrypted data
    encrypted_file = BytesIO(encrypted_data.data)
    
    return encrypted_file
