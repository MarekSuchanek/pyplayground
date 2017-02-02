from pyplayground import add


def test_add():
    assert add(1, 2, 3) == 6
    assert add(7) == 7
    assert add(-10, 10) == 0
