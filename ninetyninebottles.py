def verse(number: int) -> str:
    return (
        f"{number} bottles of beer on the wall, "
        f"{number} bottles of beer.\n"
        "Take one down and pass it around, "
        f"{number - 1} bottles of beer on the wall.\n"
    )
