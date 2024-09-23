def container(n: int) -> str:
    return "bottle" if n == 1 else "bottles"


def verse(n: int) -> str:
    match n:
        case 0:
            return (
                f"No more {container(n)} of beer on the wall, no more {container(n)} of beer.\n"
                f"Go to the store and buy some more, 99 {container(99)} of beer on the wall.\n"
            )
        case 1:
            return (
                f"1 {container(n)} of beer on the wall, 1 {container(n)} of beer.\n"
                f"Take it down and pass it around, no more {container(n-1)} of beer on the wall.\n"
            )
        case _:
            return (
                f"{n} {container(n)} of beer on the wall, {n} {container(n)} of beer.\n"
                f"Take one down and pass it around, {n-1} {container(n-1)} of beer on the wall.\n"
            )


def sing() -> str:
    return "\n".join(verse(n) for n in range(99, -1, -1))
