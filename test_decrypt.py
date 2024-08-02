import pytest
from io import BytesIO
from dataclasses import dataclass

@dataclass
class PytestScenario:
    key: str
    encrypted_content: str
    expected_decrypted_content: str

@pytest.mark.parametrize("scenario", [
    PytestScenario(
        key="""
        -----BEGIN PGP PRIVATE KEY BLOCK-----
        ... your PGP private key here ...
        -----END PGP PRIVATE KEY BLOCK-----
        """,
        encrypted_content="... encrypted content here ...",
        expected_decrypted_content="This is a test file content."
    ),
    # Add more scenarios if needed
])
def test_decrypt_file(scenario: PytestScenario[str, str, str]) -> None:
    key = BytesIO(scenario.key.encode('utf-8'))
    file = BytesIO(scenario.encrypted_content.encode('utf-8'))
    
    decrypted_file = decrypt_file(key, file)
    
    assert decrypted_file is not None
    assert decrypted_file.getvalue().decode('utf-8') == scenario.expected_decrypted_content

if __name__ == "__main__":
    pytest.main()
