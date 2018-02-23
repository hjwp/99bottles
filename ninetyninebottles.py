def verse(number):
    if number == 0:
        return (
            "No more bottles of beer on the wall, "
            "no more bottles of beer.\n"
            "Go to the store and buy some more, "
            "99 bottles of beer on the wall.\n"
        )
    if number == 1:
        return (
            "1 bottle of beer on the wall, "
            "1 bottle of beer.\n"
            "Take it down and pass it around, "
            "no more bottles of beer on the wall.\n"
        )
    if number == 2:
        return (
            "2 bottles of beer on the wall, "
            "2 bottles of beer.\n"
            "Take one down and pass it around, "
            "1 bottle of beer on the wall.\n"
        )
    if number == 6:
        return (
            "1 six-pack of beer on the wall, "
            "1 six-pack of beer.\n"
            "Take one down and pass it around, "
            "5 bottles of beer on the wall.\n"
        )
    if number == 7:
        return (
            "7 bottles of beer on the wall, "
            "7 bottles of beer.\n"
            "Take one down and pass it around, "
            "1 six-pack of beer on the wall.\n"
        )

    return (
        f"{number} bottles of beer on the wall, "
        f"{number} bottles of beer.\n"
        "Take one down and pass it around, "
        f"{number - 1} bottles of beer on the wall.\n"
    )

def sing():
    return '\n'.join(verse(n) for n in range(99, -1, -1))
