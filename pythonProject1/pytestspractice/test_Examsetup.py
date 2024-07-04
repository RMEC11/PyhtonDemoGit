import pytest


@pytest.mark.usefixtures("setup")
class Testexamsetup:
    def test_method1(self):
        print("Method 1 for Execution")

    def test_method2(self):
        print("Method 2 for Execution")