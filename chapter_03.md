
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


## Listing 3.3: Shameless Verse

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
```


* text modification:
- This method contains a case statement (the Switch Statements smell)
+ This method contains several if statements statement (the Excessive Conditionals smell)


## Listing 3.4: Verse Method Conditional

```python
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
```



* text modification:

- as in the else branch.
+ as in the default return case

- The only real difference between the 2 and else cases is the word “bottle”
+ The only real difference between the 2 and default branches is the word “bottle”


## Listing 3.5: 2 and Else Case
## Listing 3.5: number==2 and default

```python
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
```

* text notes -- several reference to "case", could be replaced with "branch", or maybe just left as-is?


## Listing 3.6: Replace Hard Coded Number

```python
if number == 2:
    return (
        f"{number} bottles of beer on the wall, "
        f"{number} bottles of beer.\n"
        "Take one down and pass it around, "
        f"{number - 1} bottle of beer on the wall.\n"
    )

return (
    f"{number} bottles of beer on the wall, "
    f"{number} bottles of beer.\n"
    "Take one down and pass it around, "
    f"{number - 1} bottles of beer on the wall.\n"
)
```

## Listing 3.7: One Difference Remains

```python
if number == 2:
    #...
    f"{number - 1} bottle of beer on the wall.\n"

return (
    #...
    f"{number - 1} bottles of beer on the wall.\n"
```

* text modification:

- To make these two lines the same, you must name this concept, create a method named after the concept, 
+ To make these two lines the same, you must name this concept, create a function named after the concept, 

(assuming we do go for a no-base-class approach)

--> several subsequent references to method also to be changed.


* text comment, section 3.7.3

> Within the context of the song, "bottle/bottles" does not represent pluralization. 

I think this is only really true once we add the six-pack requirement?

## Listing 3.8: Guess Entire Container 

```python
def container(number):
    if number == 1:
        return "bottle"
    return "bottles"
```

* comment:  in this, and in the base shameless green, I've gone for omitting the final "else" clause, which
  seems to be emerging as the "Pythonic" convention for treating the final else branch when all preceding
  ifs return early.
  there's no syntactic reason that we couldn't have it:

```python
def container(number):
    if number == 1:
        return "bottle"
    else:
        return "bottles"
```

Some people might even say that makes the logic more evident!  But in the Python world, we have this rule,
"there should be one, and preferably only one, obvious way to do things", (see
the Zen of Python), which came as a reaction against the Perl "there's more than one way to do it" philosophy.

This isn't a strong enough or well accepted enough convention that I would lose much sleep over it, if you
wanted to have "else" everywhere, though.


## unnamed listing:
```python
f"{number - 1} {container(number - 1)} of beer on the wall.\n"
```


## Listing 3.9: Empty Container Method 
## Listing 3.9: Empty Container Function

```python
def container():
    pass

```

## Listing 3.10: One Difference Remains Redux


```python
if number == 2:
    #...
    f"{number - 1} bottle of beer on the wall.\n"

return (
    #...
    f"{number - 1} bottles of beer on the wall.\n"
```

## Listing 3.11: Sparse Container Method
## Listing 3.11: Sparse Container Function

```python
def container():
    return "bottles"

```

## Listing 3.12: Sparse Container Used in Else Branch
## Listing 3.12: Sparse Container Used in Default Branch

```python
def verse(number):
    #...
    if number == 2:
        #...
        f"{number - 1} bottle of beer on the wall.\n"

    return (
        #...
        f"{number - 1} {container()} of beer on the wall.\n"

def container():
    return "bottles"
```

* comment: if I have to change too many more of these else branches into default branches i'm going to give up on my pythonic convention!!

* time taken to this point: 65 mins


## unnamed listing: premature argument in function defn

```python
def container(number):
    return "bottles"
```

* expected error:


```
TypeError: container() missing 1 required positional argument: 'number'
```


## unnamed listng: premature argument in function call

```python
f"{number - 1} {container(number - 1)} of beer on the wall.\n"
```

* expected error:

```
TypeError: container() takes 0 positional arguments but 1 was given
```



## Listing 3.13: Container With Defaulted Argument

```python
def container(number='FIXME'):
    return "bottles"
```


* Text modification:

- The above code takes an argument named number , which it defaults to the symbol :FIXME .
+ The above code takes an argument named number , which it defaults to the string "FIXME'.

- Setting it to a value like :FIXME will help you remember to do this clean-up.
+ Setting it to a value like "FIXME" will help you remember to do this clean-up.

(also some more method -> functions)


## Listing 3.14: Container With Conditional

```python
def container(number="FIXME"):
    if number == 1:
        return "bottle"
    return "bottles"
```


## unnamed listing: ternary alternative
