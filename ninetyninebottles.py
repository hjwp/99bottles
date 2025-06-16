def verse(n: int) -> str:
    return (
        f"{'No more' if n == 0 else n} bottle{'s' if n != 1 else ''} of beer on the wall, "
        + f"{'no more' if n == 0 else n} bottle{'s' if n != 1 else ''} of beer.\n"
        + (
            "Go to the store and buy some more, "
            if n == 0
            else f"Take {'it' if n == 1 else 'one'} down and pass it around, "
        )
        + f"{'no more' if n == 1 else 99 if n == 0 else n - 1} bottle{'s' if n != 2 else ''} of beer on the wall.\n"
    )


def sing() -> str:
    return "\n".join(verse(i) for i in range(99, -1, -1))
