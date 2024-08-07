import pytest
from io import BytesIO
from dataclasses import dataclass
from encrypt import encrypt_file
from typing import Any
from main import export_public_key


@dataclass
class PytestScenario:
    key: str
    file_content: str

@pytest.mark.parametrize("scenario", [
    PytestScenario(
        key= export_public_key('abc@abc.com', '12345'),
        file_content="Have a nice day."
    ),
    # Add more scenarios if needed
])
def test_encrypt_file(scenario: PytestScenario) -> None:
    key = BytesIO(scenario.key.encode('utf-8'))
    file = BytesIO(scenario.file_content.encode('utf-8'))
    
    encrypted_file = encrypt_file(key, file)
    print("Encrypted value: ", encrypted_file.getvalue())
    
    assert encrypted_file is not None
    assert len(encrypted_file.getvalue()) > 0

if __name__ == "__main__":
    pytest.main()
