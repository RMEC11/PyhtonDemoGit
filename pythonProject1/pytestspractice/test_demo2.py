import pytest


@pytest.mark.xfail
def test_loginwithpass():
    msg="login with pass"
    assert msg == "Good Morning","Test string doesn't match"

@pytest.mark.smoke
@pytest.mark.skip
def test_Secondmethod():
    a=4
    b=2
    assert a-2 == b, "sub doesn't match"
