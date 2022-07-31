'''
Для запуска набрать в терминале
python -m pytest 103_pytest.py
pytest -q 103_pytest.py
'''

import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
    
    
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

    
if __name__ == '__main__':
    test_mytest()
    
    
