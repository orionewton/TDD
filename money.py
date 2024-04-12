from typing import Self


class Money:
    def __init__(self, val: int):
        self.amount = val

    def times(self, mult):
        return Money(self.amount * mult)

    def __eq__(self, b: Self):
        return self.amount == b.amount and type(b) is type(self)

    @staticmethod
    def dollar(val):
        return Dollar(val)

    @staticmethod
    def franc(val):
        return Franc(val)


class Dollar(Money):
    def times(self, mult):
        return Dollar(self.amount * mult)


class Franc(Money):
    def times(self, mult):
        return Franc(self.amount * mult)
