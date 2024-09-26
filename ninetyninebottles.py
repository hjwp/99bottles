from dataclasses import dataclass
from typing import Iterable
import itertools


@dataclass
class Bottles:
    container: str
    quantity: str
    action: str
    pronoun: str


def _bottles_for(n: int) -> Bottles:
    match n:
        case 0:
            return Bottles(
                "bottles", "no more", "Go to the store and buy some more", ""
            )
        case 1:
            return Bottles("bottle", "1", "Take it down and pass it around", "it")
        case _:
            return Bottles("bottles", str(n), "Take one down and pass it around", "one")


def verse(n: int, next_n: int = -999) -> str:
    bottles, next_bottles = _bottles_for(n), _bottles_for(next_n)
    return (
        f"{bottles.quantity.capitalize()} {bottles.container} of beer on the wall, "
        f"{bottles.quantity} {bottles.container} of beer."
        "\n"
        f"{bottles.action}, "
        f"{next_bottles.quantity} {next_bottles.container} of beer on the wall."
        "\n"
    )


def _sing() -> Iterable[str]:
    nums = itertools.cycle(range(99, -1, -1))
    nums2 = itertools.cycle(range(99, -1, -1))
    for n, next_n in zip(nums, nums2):
        yield verse(n, next_n=next_n)


def sing() -> str:
    return "\n".join(_sing())
