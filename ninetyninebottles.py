def verse(n):
    match n:
        case 0:
            return (
                "No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
            )
        case 1:
            return (
                "1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall.\n"
            )
        case 2:
            return (
                "2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, 1 bottle of beer on the wall.\n"
            )
        case _:
            return (
                f"{n} bottles of beer on the wall, {n} bottles of beer.\n"
                f"Take one down and pass it around, {n-1} bottles of beer on the wall.\n"
            )


def sing():
    return "\n".join(verse(n) for n in range(99, -1, -1))
