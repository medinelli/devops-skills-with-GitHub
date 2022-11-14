from mylib.calculate import add, substract, multiply, divide


def test_add():
    assert add(3, 5) == 8


# build a test for substract
def test_substract():
    assert substract(10, 5) == 5


def test_multiply():
    assert multiply(5, 5) == 25
    assert multiply(4, 4) == 16


def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
