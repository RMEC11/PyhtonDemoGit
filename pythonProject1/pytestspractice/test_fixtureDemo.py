import pytest


@pytest.mark.usefixtures("setup")
class Example:
    def test_method1(self):
        print("Method1 between before and after execution message")
