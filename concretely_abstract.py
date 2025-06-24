from dataclasses import dataclass


@dataclass
class Round:
    bottles: int

    def __str__(self) -> str:
        return self.challenge() + self.response()

    def challenge(self) -> str:
        return (
            self.bottles_of_beer().capitalize()
            + " "
            + self.on_wall()
            + ", "
            + self.bottles_of_beer()
            + ".\n"
        )

    def response(self) -> str:
        return (
            self.go_to_the_store_or_take_one_down()
            + ", "
            + self.bottles_of_beer()
            + " "
            + self.on_wall()
            + ".\n"
        )

    def bottles_of_beer(self) -> str:
        return f"{self.anglicized_bottle_count()} {self.pluralized_bottle_form()} of {self.beer()}"

    def beer(self) -> str:
        return "beer"

    def on_wall(self) -> str:
        return "on the wall"

    def pluralized_bottle_form(self) -> str:
        return "bottle" if self.last_beer() else "bottles"

    def anglicized_bottle_count(self) -> str:
        return "no more" if self.all_out() else str(self.bottles)

    def go_to_the_store_or_take_one_down(self) -> str:
        if self.all_out():
            self.bottles = 99
            return self.buy_new_beer()
        else:
            lyris = self.drink_beer()
            self.bottles -= 1
            return lyris

    def buy_new_beer(self) -> str:
        return "Go to the store and buy some more"

    def drink_beer(self) -> str:
        return f"Take {self.it_or_one()} down and pass it around"

    def it_or_one(self) -> str:
        return "it" if self.last_beer() else "one"

    def all_out(self) -> bool:
        return self.bottles == 0

    def last_beer(self) -> bool:
        return self.bottles == 1


def verse(n: int) -> str:
    return str(Round(n))


def sing() -> str:
    return "\n".join(verse(i) for i in range(99, -1, -1))
