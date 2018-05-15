def calculate(a,b):
    c = a + b
    return c

def test_step01():
    result = calculate(2,3)
    assert result == 5

def test_step02():
    result = calculate(5,3)
    assert result == 8

def test_step03():
    result = calculate(8,4)
    assert result == 12
