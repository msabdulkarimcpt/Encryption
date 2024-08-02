import pytest
from io import BytesIO
from dataclasses import dataclass

@dataclass
class PytestScenario:
    key: str
    file_content: str

@pytest.mark.parametrize("scenario", [
    PytestScenario(
        key="""
        -----BEGIN PGP PUBLIC KEY BLOCK-----
        ... your PGP public key here ...
        -----END PGP PUBLIC KEY BLOCK-----
        """,
        file_content="This is a test file content."
    ),
    # Add more scenarios if needed
])
def test_encrypt_file(scenario: PytestScenario[str, str]) -> None:
    key = BytesIO(scenario.key.encode('utf-8'))
    file = BytesIO(scenario.file_content.encode('utf-8'))
    
    encrypted_file = encrypt_file(key, file)
    
    assert encrypted_file is not None
    assert len(encrypted_file.getvalue()) > 0

if __name__ == "__main__":
    pytest.main()
