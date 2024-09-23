def container(n: int) -> str:
    return "bottle" if n == 1 else "bottles"


def quantity(n: int) -> str:
    return "no more" if n == 0 else str(n)


def verse(n: int) -> str:
    match n:
        case 0:
            return (
                f"No more {container(n)} of beer on the wall, no more {container(n)} of beer.\n"
                f"Go to the store and buy some more, 99 {container(99)} of beer on the wall.\n"
            )
        case _:
            pronoun = "it" if n == 1 else "one"
            return (
                f"{n} {container(n)} of beer on the wall, {n} {container(n)} of beer.\n"
                f"Take {pronoun} down and pass it around, {quantity(n-1)} {container(n-1)} of beer on the wall.\n"
            )


def sing() -> str:
    return "\n".join(verse(n) for n in range(99, -1, -1))
