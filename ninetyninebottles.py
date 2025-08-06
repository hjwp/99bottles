from __future__ import annotations

from dataclasses import dataclass


def verse(number: int) -> str:
    this_bottles = Bottles.build(number)
    next_bottles = Bottles.build(
        this_bottles.next_number  # TODO: this feels awkward
    )
    line1 = f"{this_bottles} of beer on the wall, {this_bottles} of beer"
    line2 = f"{this_bottles.action}, {next_bottles} of beer on the wall"
    return f"{line1.capitalize()}.\n{line2.capitalize()}.\n"


@dataclass
class Bottles:
    _num_bottles: int
    _pronoun: str = "one"
    container: str = "bottles"

    @classmethod
    def build(cls, num_bottles: int) -> Bottles:
        if num_bottles == 0:
            return NoBottles()
        if num_bottles == 1:
            return OneBottle()
        return cls(num_bottles)

    def __str__(self) -> str:
        return f"{self.quantity} {self.container}"

    @property
    def quantity(self) -> str:
        return str(self._num_bottles)

    @property
    def action(self) -> str:
        return f"take {self._pronoun} down and pass it around"

    @property
    def next_number(self) -> int:
        return self._num_bottles - 1


@dataclass
class NoBottles(Bottles):
    _num_bottles: int = 0
    quantity: str = "no more"
    action: str = "go to the store and buy some more"
    next_number: int = 99


@dataclass
class OneBottle(Bottles):
    _num_bottles: int = 1
    _pronoun: str = "it"
    container: str = "bottle"


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
