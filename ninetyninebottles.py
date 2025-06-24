def verse(number: int) -> str:
    match number:
        case 0:
            return (
                "No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.\n"
            )
        case 1:
            return (
                "1 bottle of beer on the wall, "
                "1 bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
            )
        case 2:
            return (
                "2 bottles of beer on the wall, "
                "2 bottles of beer.\n"
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.\n"
            )
        case _:
            return (
                f"{number} bottles of beer on the wall, "
                f"{number} bottles of beer.\n"
                "Take one down and pass it around, "
                f"{number - 1} bottles of beer on the wall.\n"
            )

def verses(start: int, end: int) -> str:
    return "\n".join(verse(n) for n in range(start, end - 1, -1))
