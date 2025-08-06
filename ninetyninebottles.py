from dataclasses import dataclass


def verse(number: int) -> str:
    this_bottles = Bottles(number)
    next_bottles = Bottles(
        this_bottles.next_number  # TODO: this feels awkward
    )
    line1 = f"{this_bottles} of beer on the wall, {this_bottles} of beer"
    line2 = f"{this_bottles.action}, {next_bottles} of beer on the wall"
    return f"{line1.capitalize()}.\n{line2.capitalize()}.\n"


@dataclass
class Bottles:
    num_bottles: int

    def __str__(self) -> str:
        return f"{self.quantity} {self.container}"

    @property
    def container(self) -> str:
        if self.num_bottles == 1:
            return "bottle"
        return "bottles"

    @property
    def _pronoun(self) -> str:
        if self.num_bottles == 1:
            return "it"
        return "one"

    @property
    def quantity(self) -> str:
        if self.num_bottles == 0:
            return "no more"
        return str(self.num_bottles)

    @property
    def action(self) -> str:
        if self.num_bottles == 0:
            return "go to the store and buy some more"
        return f"take {self._pronoun} down and pass it around"

    @property
    def next_number(self) -> int:
        if self.num_bottles == 0:
            return 99
        return self.num_bottles - 1


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
