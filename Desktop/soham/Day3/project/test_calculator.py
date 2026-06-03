import pytest 
from calculator import add 
from calculator import sub
def test_add():
    assert add(4,5)==9
    assert add(1,2)==4 
def test_sub():
    assert sub(5,4)==1
    assert sub(1,2)==1
    assert sub(10,1)==7 