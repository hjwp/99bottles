from __future__ import annotations

from dataclasses import dataclass


def song() -> str:
    return verses(99, 0)


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def verse(number: int) -> str:
    this_bottles = Bottles.for_(number)
    line1 = f"{this_bottles} of beer on the wall, {this_bottles} of beer"
    line2 = f"{this_bottles.action}, {this_bottles.next} of beer on the wall"
    return f"{line1.capitalize()}.\n{line2.capitalize()}.\n"


@dataclass(frozen=True)
class Bottles:
    _num_bottles: int
    _pronoun: str = "one"
    container: str = "bottles"

    @staticmethod
    def for_(num_bottles: int) -> Bottles:
        match num_bottles:
            case 0:
                return NoBottles()
            case 1:
                return OneBottle()
            case _:
                return Bottles(num_bottles)

    def __str__(self) -> str:
        return f"{self.quantity} {self.container}"

    @property
    def quantity(self) -> str:
        return str(self._num_bottles)

    @property
    def action(self) -> str:
        return f"take {self._pronoun} down and pass it around"

    @property
    def next(self) -> Bottles:
        return Bottles.for_(self._num_bottles - 1)


@dataclass(frozen=True)
class NoBottles(Bottles):
    _num_bottles: int = 0
    quantity: str = "no more"
    action: str = "go to the store and buy some more"

    @property
    def next(self) -> Bottles:
        return Bottles(99)


@dataclass(frozen=True)
class OneBottle(Bottles):
    _num_bottles: int = 1
    _pronoun: str = "it"
    container: str = "bottle"
