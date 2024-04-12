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
    assert Dollar(5) == Dollar(5)
    assert not Dollar(5) == Dollar(6)
    assert Franc(5) == Franc(5)
    assert not Franc(5) == Franc(6)
    assert not Dollar(5) == Franc(5)
