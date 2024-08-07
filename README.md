# Encryption

PGP Encryption and Decryption

# Encrpyt:

Files encrypted using a PGP key.
Verify the function accepts the key and a file(unencrypted) and outputs an encrypted file.

encrypt function as:
def encrypt_file(key: IO, file: IO) -> IO:

encrypt test function as:
def test_encrypt_file(scenario: PytestScenario[str, str,str,str]) -> None:

# Decrpyt:

Files decrypted using a PGP key.
Verify the function accepts the key and a file encrypted and outputs an decrypted file.

decrypt function as:
def decrypt_file(key: IO, file: IO) -> IO:

decrypt test function as:
def test_decrypt_file(scenario: PytestScenario[str, str]) -> None:
