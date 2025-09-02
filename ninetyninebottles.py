from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

SongVerse = Callable[[int], str]


def song(verse: SongVerse | None = None) -> str:
    if verse is None:
        verse = bottles_verse
    return verses(verse, 99, 0)


def verses(verse: SongVerse, start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def bottles_verse(number: int) -> str:
    this_bottles = _bottles_for(number)
    line1 = f"{this_bottles} of beer on the wall, {this_bottles} of beer"
    line2 = f"{this_bottles.action}, {this_bottles.next} of beer on the wall"
    return f"{line1.capitalize()}.\n{line2.capitalize()}.\n"


def _bottles_for(num_bottles: int) -> Bottles:
    match num_bottles:
        case 0:
            return NoBottles()
        case 1:
            return OneBottle()
        case _:
            return Bottles(num_bottles)


@dataclass(frozen=True)
class Bottles:
    _num_bottles: int
    _pronoun: str = "one"
    container: str = "bottles"

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
        return _bottles_for(self._num_bottles - 1)


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
