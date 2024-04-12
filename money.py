from typing import Self


class Dollar:
    def __init__(self, val: int):
        self.amount = val

    def times(self, mult):
        return self.amount * mult

    def equals(self, b: Self):
        return self.amount == b.amount
