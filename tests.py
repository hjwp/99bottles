from pathlib import Path

from ninetyninebottles import song, bottles_verse, verses


def test_the_first_verse() -> None:
    expected = (
        "99 bottles of beer on the wall, "
        "99 bottles of beer.\n"
        "Take one down and pass it around, "
        "98 bottles of beer on the wall.\n"
    )
    assert bottles_verse(99) == expected


def test_another_verse() -> None:
    expected = (
        "3 bottles of beer on the wall, "
        "3 bottles of beer.\n"
        "Take one down and pass it around, "
        "2 bottles of beer on the wall.\n"
    )
    assert bottles_verse(3) == expected


def test_verse_2() -> None:
    expected = (
        "2 bottles of beer on the wall, "
        "2 bottles of beer.\n"
        "Take one down and pass it around, "
        "1 bottle of beer on the wall.\n"
    )
    assert bottles_verse(2) == expected


def test_verse_1() -> None:
    expected = (
        "1 bottle of beer on the wall, "
        "1 bottle of beer.\n"
        "Take it down and pass it around, "
        "no more bottles of beer on the wall.\n"
    )
    assert bottles_verse(1) == expected


def test_verse_0() -> None:
    expected = (
        "No more bottles of beer on the wall, "
        "no more bottles of beer.\n"
        "Go to the store and buy some more, "
        "99 bottles of beer on the wall.\n"
    )
    assert bottles_verse(0) == expected


def test_a_couple_verses() -> None:
    expected = (
        "99 bottles of beer on the wall, "
        "99 bottles of beer.\n"
        "Take one down and pass it around, "
        "98 bottles of beer on the wall.\n"
        "\n"
        "98 bottles of beer on the wall, "
        "98 bottles of beer.\n"
        "Take one down and pass it around, "
        "97 bottles of beer on the wall.\n"
    )
    assert verses(bottles_verse, 99, 98) == expected


def test_a_few_verses() -> None:
    expected = (
        "2 bottles of beer on the wall, "
        + "2 bottles of beer.\n"
        + "Take one down and pass it around, "
        + "1 bottle of beer on the wall.\n"
        + "\n"
        + "1 bottle of beer on the wall, "
        + "1 bottle of beer.\n"
        + "Take it down and pass it around, "
        + "no more bottles of beer on the wall.\n"
        + "\n"
        + "No more bottles of beer on the wall, "
        + "no more bottles of beer.\n"
        + "Go to the store and buy some more, "
        + "99 bottles of beer on the wall.\n"
    )
    assert verses(bottles_verse, 2, 0) == expected


def test_song() -> None:
    assert song() == Path("full-song.txt").read_text()
