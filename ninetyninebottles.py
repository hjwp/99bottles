from dataclasses import dataclass
from typing import Iterable
import itertools


@dataclass
class Bottles:
    name: str
    action: str

    def __str__(self) -> str:
        return f"{self.name}"


def _bottles_for(n: int) -> Bottles:
    match n:
        case 0:
            return Bottles("no more bottles", "go to the store and buy some more")
        case 1:
            return Bottles("1 bottle", "take it down and pass it around")
        case 6:
            return Bottles("one six-pack", "take one down and pass it around")
        case _:
            return Bottles(f"{n} bottles", "take one down and pass it around")


def verse(n: int, next_n: int = -999) -> str:
    bottles, next_bottles = _bottles_for(n), _bottles_for(next_n)
    return "".join(
        [
            f"{bottles} of beer on the wall, ".capitalize(),
            f"{bottles} of beer.",
            "\n",
            f"{bottles.action}, ".capitalize(),
            f"{next_bottles} of beer on the wall.",
            "\n",
        ]
    )


def _sing(start: int) -> Iterable[str]:
    nums = itertools.cycle(range(start, -1, -1))
    nums2 = itertools.cycle(range(start, -1, -1))
    next(nums2)
    for n, next_n in zip(nums, nums2):
        yield verse(n, next_n)
        if next_n == start:
            return


def sing() -> str:
    return "\n".join(_sing(99))
