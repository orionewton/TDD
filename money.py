from typing import Self


class Currency:
    def __init__(self, val: int):
        self.amount = val

    def times(self, mult):
        return self.amount * mult

    def __eq__(self, b: Self):
        return self.amount == b.amount


class Dollar(Currency):
    pass


class Franc(Currency):
    pass
