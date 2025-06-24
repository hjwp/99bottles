from ninetyninebottles import verse


def test_the_first_verse() -> None:
    expected = (
        "99 bottles of beer on the wall, "
        "99 bottles of beer.\n"
        "Take one down and pass it around, "
        "98 bottles of beer on the wall.\n"
    )
    assert verse(99) == expected

def test_another_verse() -> None:
    expected = (
        "3 bottles of beer on the wall, "
        "3 bottles of beer.\n"
        "Take one down and pass it around, "
        "2 bottles of beer on the wall.\n"
    )
    assert verse(3) == expected
