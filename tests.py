from money import Dollar


def test_multiplication():
    five = Dollar(5)
    product = Dollar(five.times(2))
    assert product.amount == 10
    product = Dollar(five.times(3))
    assert product.amount == 15


def test_equality():
    a = Dollar(5)
    b = Dollar(5)
    c = Dollar(6)
    assert a.equals(b)
    assert not a.equals(c)

