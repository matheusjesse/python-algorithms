from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "AABBCC"
    assert encrypt_message(message, -1) == "CCBBAA"

    assert encrypt_message(message, 3) == "BAA_CCB"

    assert encrypt_message(message, 4) == "CC_BBAA"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "string")
