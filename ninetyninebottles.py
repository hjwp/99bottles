class Bottles:
    """
    Represents a number of bottles (maybe zero),
    how to talk about them, and how to get the next number of bottles
    """
    def __init__(self, number):
        self.number = number

    def __str__(self):
        if self.number == 0:
            return 'no more bottles'
        if self.number == 1:
            return '1 bottle'
        return f'{self.number} bottles'

    @property
    def action(self):
        if self.number == 0:
            return 'go to the store and buy some more'
        return f'take {self.pronoun} down and pass it around'

    @property
    def pronoun(self):
        if self.number == 1:
            return 'it'
        return 'one'

    @property
    def successor(self):
        if self.number == 0:
            return Bottles(99)
        return Bottles(self.number - 1)


def verse(n):
    bottles = Bottles(n)
    return (
        f"{bottles} of beer on the wall, {bottles} of beer.\n".capitalize() +
        f"{bottles.action}, {bottles.successor} of beer on the wall.\n".capitalize()
    )

def sing():
    return '\n'.join(verse(n) for n in range(99, -1, -1))
