# Day 18:  165. Understanding Turtle Graphics and How to use the Documentation

## Resources

[RGB colors](https://www.w3schools.com/colors/colors_rgb.asp)

## python Turtle docs

[link to docs](https://docs.python.org/3/library/turtle.html)

### Colors

[link to colors](https://trinket.io/docs/colors)

## importing modules

#### regular form
```python
import turtle

tim = turtle.Turtle()
```

#### simple form

Avoid the turtle.Turtle repetition
```python
from turtle import Turtle

tim = Turtle()
```

#### short form
Shorting the name of a module
```python
import turtle as t

tim = t.Turtle()
```

## Installing package

#### Install a package that doesn't exist in the python modules

for example if you want to import the heroes' module you need first, search it in the [python library index](https://pypi.org/)

and then write in the terminal to install in your computer the module
```bash
pip install heroes
```

And then you'll import it as you did with other modules.

## TUPLE

Is a data type like a list but the values have immutability. You write it in stone