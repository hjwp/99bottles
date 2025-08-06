from __future__ import annotations

from dataclasses import dataclass


def verse(number: int) -> str:
    this_bottles = Bottles.build(number)
    next_bottles = Bottles(
        this_bottles.next_number  # TODO: this feels awkward
    )
    line1 = f"{this_bottles} of beer on the wall, {this_bottles} of beer"
    line2 = f"{this_bottles.action}, {next_bottles} of beer on the wall"
    return f"{line1.capitalize()}.\n{line2.capitalize()}.\n"


class Bottles:
    def __init__(self, num_bottles: int) -> None:
        self._num_bottles = num_bottles

    @classmethod
    def build(cls, num_bottles: int) -> Bottles:
        if num_bottles == 0:
            return NoBottles(0)
        return cls(num_bottles)

    def __str__(self) -> str:
        return f"{self.quantity} {self.container}"

    @property
    def container(self) -> str:
        if self._num_bottles == 1:
            return "bottle"
        return "bottles"

    @property
    def _pronoun(self) -> str:
        if self._num_bottles == 1:
            return "it"
        return "one"

    @property
    def quantity(self) -> str:
        if self._num_bottles == 0:
            return "no more"
        return str(self._num_bottles)

    @property
    def action(self) -> str:
        if self._num_bottles == 0:
            return "go to the store and buy some more"
        return f"take {self._pronoun} down and pass it around"

    @property
    def next_number(self) -> int:
        if self._num_bottles == 0:
            return 99
        return self._num_bottles - 1


@dataclass
class NoBottles(Bottles):
    _num_bottles: int
    quantity: str = "no more"
    action: str = "go to the store and buy some more"
    next_number: int = 99


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
