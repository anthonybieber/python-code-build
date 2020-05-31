# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

def test_incorrect():
    assert func(8) == 9

def test_bullshit():
    assert 'hello' == 'hello'
