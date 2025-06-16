from textwrap import dedent


def _describe_bottles(n: int) -> str:
    if n == 0:
        return "no more bottles"
    elif n == 1:
        return "1 bottle"
    else:
        return f"{n} bottles"


def verse(n: int) -> str:
    these_bottles = _describe_bottles(n)
    shelf = (
        f"{these_bottles} of beer on the wall, {these_bottles} of beer.".capitalize()
    )

    if n == 0:
        action = "Go to the store and buy some more"
        next_bottles = _describe_bottles(99)
    else:
        next_bottles = _describe_bottles(n - 1)
        this_bottle = "it" if n == 1 else "one"
        action = f"Take {this_bottle} down and pass it around"

    return f"{shelf}\n{action}, {next_bottles} of beer on the wall.\n"


def sing() -> str:
    return "\n".join(verse(i) for i in range(99, -1, -1))
