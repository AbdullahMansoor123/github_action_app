from src.math_operation import add, sub, multi

def test_add():
    assert add(2,3) == 5
    assert add(3,-2) == 1
    assert add(-1,-2) == -3

def test_sub():
    assert sub(2, 3) == -1
    assert sub(3, -2) == 5
    assert sub(5,2) == 3

def test_multi():
    assert multi(5,2) == 10
    assert multi(-1,-6) == 6
    assert multi(-4,5) == 20


