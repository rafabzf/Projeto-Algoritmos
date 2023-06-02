from challenges.challenge_encrypt_message import encrypt_message
import pytest



def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('string', 'string')

    with pytest.raises(TypeError):
        encrypt_message(120, 100)

    assert encrypt_message('String', 0) == 'gnirtS'
    assert encrypt_message('String', -4) == 'gnirtS'
    assert encrypt_message('String', 10) == 'gnirtS'
    assert encrypt_message('String', 11) == 'gnirtS'
    assert encrypt_message('String', 3) == 'rtS_gni'
    assert encrypt_message('String', 4) == 'gn_irtS'
