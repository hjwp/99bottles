def verse(number: int) -> str:
    match number:
        case 0:
            return (
                f"No more {_container(number)} of beer on the wall, "
                f"no more {_container(number)} of beer.\n"
                f"Go to the store and buy some more, "
                f"99 {_container(number - 1)} of beer on the wall.\n"
            )
        case 1:
            return (
                f"{number} {_container(number)} of beer on the wall, "
                f"{number} {_container(number)} of beer.\n"
                f"Take it down and pass it around, "
                f"no more {_container(number - 1)} of beer on the wall.\n"
            )
        case _:
            return (
                f"{number} {_container(number)} of beer on the wall, "
                f"{number} {_container(number)} of beer.\n"
                "Take one down and pass it around, "
                f"{number - 1} {_container(number - 1)} of beer on the wall.\n"
            )


def _container(number: int) -> str:
    return "bottle" if number == 1 else "bottles"


def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))


def song() -> str:
    return verses(99, 0)
