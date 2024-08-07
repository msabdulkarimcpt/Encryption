import pytest
from io import BytesIO
from dataclasses import dataclass
from decrypt import decrypt_file
from encrypt import encrypt_file
from main import export_private_key, export_public_key

def get_encrypted_content(email: str, passphrase: str, file_content:str) -> str:
    public_key = export_public_key(email, passphrase)
    key_in_bytes = BytesIO(public_key.encode('utf-8'))
    file = BytesIO(file_content.encode('utf-8'))
    encrypted_file = encrypt_file(key_in_bytes, file)
    encrypted_data = (encrypted_file.getvalue()).decode('utf-8')
    return encrypted_data


@dataclass
class PytestScenario:
    key: str
    passphrase : str
    encrypted_content: str
    expected_decrypted_content: str

@pytest.mark.parametrize("scenario", [
    PytestScenario(
        key=export_private_key('abc@abc.com', '12345'),
        passphrase = '12345',
        encrypted_content=get_encrypted_content('abc@abc.com', '12345',"Have a nice day."),
        expected_decrypted_content="Have a nice day."
    ),
])
def test_decrypt_file(scenario: PytestScenario) -> None:
    key = BytesIO(scenario.key.encode('utf-8'))
    file = BytesIO(scenario.encrypted_content.encode('utf-8'))
    
    decrypted_file = decrypt_file(key, file, scenario.passphrase)
    
    assert decrypted_file is not None
    assert decrypted_file.getvalue().decode('utf-8') == scenario.expected_decrypted_content

if __name__ == "__main__":
    pytest.main()
