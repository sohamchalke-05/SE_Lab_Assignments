import pytest
from otp_program import generate_otp  # Replace with actual file/module name

def test_generate_otp_length():
    otp = generate_otp(6)
    assert len(otp) == 6

    otp = generate_otp(4)
    assert len(otp) == 4

    with pytest.raises(ValueError):
        generate_otp(9)  # Length exceeds 8

def test_generate_otp_content():
    otp = generate_otp(6)
    assert otp.isdigit()
