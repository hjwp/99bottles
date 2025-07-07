def verse(number: int) -> str:
    match number:
        case 0:
            return (
                f"{_quantity(number)} {_container(number)} of beer on the wall, ".capitalize()
                + f"{_quantity(number)} {_container(number)} of beer.\n"
                + f"{_action(number)}, ".capitalize()
                + f"99 {_container(number - 1)} of beer on the wall.\n"
            )
        case _:
            return (
                f"{_quantity(number)} {_container(number)} of beer on the wall, ".capitalize()
                + f"{number} {_container(number)} of beer.\n"
                + f"{_action(number)}, ".capitalize()
                + f"{_quantity(number - 1)} {_container(number - 1)} of beer on the wall.\n"
            )


def _container(number: int) -> str:
    return "bottle" if number == 1 else "bottles"


def _pronoun(number: int) -> str:
    return "it" if number == 1 else "one"


def _quantity(number: int) -> str:
    return "no more" if number == 0 else str(number)


def _action(number: int) -> str:
    if number == 0:
        return f"go to the store and buy some more"
    return f"take {_pronoun(number)} down and pass it around"


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
