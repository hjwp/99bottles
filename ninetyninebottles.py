def container(n: int) -> str:
    return "bottle" if n == 1 else "bottles"


def quantity(n: int) -> str:
    return "no more" if n == 0 else str(n)


def verse(n: int) -> str:
    match n:
        case 0:
            next_n = 99
            action = "Go to the store and buy some more"
        case _:
            next_n = n - 1
            pronoun = "it" if n == 1 else "one"
            action = f"Take {pronoun} down and pass it around"

    return (
        f"{quantity(n).capitalize()} {container(n)} of beer on the wall, "
        f"{quantity(n)} {container(n)} of beer."
        "\n"
        f"{action}, "
        f"{quantity(next_n)} {container(next_n)} of beer on the wall."
        "\n"
    )


def sing() -> str:
    return "\n".join(verse(n) for n in range(99, -1, -1))
