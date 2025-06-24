def verse(number: int) -> str:
    if number == 2:
        return (
            f"{2} bottles of beer on the wall, "
            f"{2} bottles of beer.\n"
            "Take one down and pass it around, "
            f"{1} bottle of beer on the wall.\n"
        )
    return (
        f"{number} bottles of beer on the wall, "
        f"{number} bottles of beer.\n"
        "Take one down and pass it around, "
        f"{number - 1} bottles of beer on the wall.\n"
    )
