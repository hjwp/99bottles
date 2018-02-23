
## Listing 3.1: Shameless Green

```python
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

    return (
        f"{number} bottles of beer on the wall, "
        f"{number} bottles of beer.\n"
        "Take one down and pass it around, "
        f"{number - 1} bottles of beer on the wall.\n"
    )

def sing():
    return '\n'.join(verse(n) for n in range(99, -1, -1))
```

* Text modification:

- Conditionals are the bane of OO. Shameless Green contains a case statement, and within its branches,
+ Conditionals are the bane of OO. Shameless Green contains 3 if statements, and within the branches,


## Listing 3.2: Compounding Conditional Sins

```python
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
```

> "Open" is short for "Open/Closed," which in turn is short for "open for extension and closed for modification."

* comment: not sure I really understand what's meant by open/closed...
  is it: open to a new requirement =  I can implement the new requirement without adding too much
  extra complexity?  and the reason we're not open here is bc we need to go from 4 ifs to 6 ifs?
  whereas once we're done with the OO design, we only need to go from 2 ifs to 3 ifs?

* text modification
- Also, if you prefer your examples in Ruby, you may be interested in Jay Fields'
version of the book.
+  python replacement tbc? or cut?

