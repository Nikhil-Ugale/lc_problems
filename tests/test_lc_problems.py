from src.implementstr import strStr
from src.add import addTwoNumbers
def test_strStr():
    assert strStr('hello','ll')==2

def test1_strStr():
    assert strStr('hello','o')==4

def test_addTwoNumbers():
    assert addTwoNumbers(23,5)==28