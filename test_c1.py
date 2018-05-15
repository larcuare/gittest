def calculate(a,b):
    c = a + b
    return c

def test_case01():
    result = calculate(3,3)
    assert result == 6

def test_case02():
    result = calculate(3,5)
    assert result == 7