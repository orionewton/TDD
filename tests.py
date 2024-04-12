from money import Dollar, Franc


def test_multiplication():
    five = Dollar(5)
    assert Dollar(10) == Dollar(five.times(2))
    assert Dollar(15) == Dollar(five.times(3))


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == Franc(five.times(2))
    assert Franc(15) == Franc(five.times(3))


def test_equality():
    a = Dollar(5)
    b = Dollar(5)
    c = Dollar(6)
    assert a == b
    assert not a == c
