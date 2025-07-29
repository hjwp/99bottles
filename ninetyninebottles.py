from dataclasses import dataclass


def verse(number: int) -> str:
    bn = BottleNumber(number)
    next_bn = BottleNumber(bn.next())
    return (
        f"{bn.quantity().capitalize()} {bn.container()} of beer on the wall, "
        f"{bn.quantity()} {bn.container()} of beer.\n"
        f"{bn.action().capitalize()}, "
        f"{next_bn.quantity()} {next_bn.container()} of beer on the wall.\n"
    )


@dataclass
class BottleNumber:
    num_bottles: int

    def container(self) -> str:
        if self.num_bottles == 1:
            return "bottle"
        return "bottles"

    def _pronoun(self) -> str:
        if self.num_bottles == 1:
            return "it"
        return "one"

    def quantity(self) -> str:
        if self.num_bottles == 0:
            return "no more"
        return str(self.num_bottles)

    def action(self) -> str:
        if self.num_bottles == 0:
            return "go to the store and buy some more"
        return f"take {self._pronoun()} down and pass it around"

    def next(self) -> int:
        if self.num_bottles == 0:
            return 99
        return self.num_bottles - 1


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
