# Any Pytest file name should start with test_ or end with _test
# Any pytest method name should start with test
# Any code should wrapped in method
import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("Hello Abhishek")

def test_loginwithotp():
    print("Login with OTP")