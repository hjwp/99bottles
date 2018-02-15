class Bottles:
    """
    Represents a number of bottles (maybe zero),
    how to talk about them, and how to get the next number of bottles
    """
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number} bottles'

    @property
    def action(self):
        return f'take {self.pronoun} down and pass it around'

    @property
    def pronoun(self):
        return 'one'

    @property
    def successor(self):
        return Bottles.for_number(self.number - 1)

    @staticmethod
    def for_number(number):
        if number == 0:
            return NoBottles()
        if number == 1:
            return OneBottle()
        return Bottles(number)


class NoBottles(Bottles):
    def __init__(self):
        self.number = 0

    def __str__(self):
        return 'no more bottles'

    @property
    def action(self):
        return 'go to the store and buy some more'

    @property
    def successor(self):
        return Bottles.for_number(99)


class OneBottle(Bottles):
    def __init__(self):
        self.number = 1

    def __str__(self):
        return '1 bottle'

    @property
    def pronoun(self):
        return 'it'


def verse(n):
    bottles = Bottles.for_number(n)
    return (
        f"{bottles} of beer on the wall, {bottles} of beer.\n".capitalize() +
        f"{bottles.action}, {bottles.successor} of beer on the wall.\n".capitalize()
    )

def sing():
    return '\n'.join(verse(n) for n in range(99, -1, -1))
