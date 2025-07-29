def verse(number: int) -> str:
    return (
        f"{_quantity(number).capitalize()} {_container(number)} of beer on the wall, "
        f"{_quantity(number)} {_container(number)} of beer.\n"
        f"{_action(number).capitalize()}, "
        f"{_quantity(_next(number))} {_container(_next(number))} of beer on the wall.\n"
    )


def _container(number: int) -> str:
    if number == 1:
        return "bottle"
    return "bottles"


def _pronoun(number: int) -> str:
    if number == 1:
        return "it"
    return "one"


def _quantity(number: int) -> str:
    if number == 0:
        return "no more"
    return str(number)


def _action(number: int) -> str:
    if number == 0:
        return "go to the store and buy some more"
    return f"take {_pronoun(number)} down and pass it around"


def _next(number: int) -> int:
    if number == 0:
        return 99
    return number - 1


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
