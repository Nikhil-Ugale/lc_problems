from src.implementstr import strStr
from src.add import addTwoNumbers
from src.pascal import pascalTriangle

def test_strStr():
    assert strStr('hello','ll')==2

def test1_strStr():
    assert strStr('hello','o')==4

def test_addTwoNumbers():
    assert addTwoNumbers(23,5)==28

def test_pascalTriangle():
    assert pascalTriangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]