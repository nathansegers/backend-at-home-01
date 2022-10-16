# Assignment 1 -- Extensive Python Functionalities

## Introduction

This assignment will guide you through using the different Python functionalities the Theory class was about.
This goes through Inheritance in Python, so you learn about Object Oriented Programming.
By using Decorators, List and Dict comprehensions and Generartors, combined with the knowledge of Inheritance, you will be able to create a simple project.

## Assignment explanation

The assignment is about creating a simple game.
We will create a chess game, but only a textual representation in the dictionary states.
Later on, we can re-use this project in some of our other classes.

The Chess game will be far from finished, but it will give you a good idea of Inheritance in Python. You could work it out as far as you think is necessary to understand all the concepts.

For those who want to experiment with the Chess games, you can use the `Pygame` library to create a graphical representation of the game. Numerous libraries exist that can be used to help with playing Chess.

## Getting started

Make sure you install Poetry using the help in the theory class.
We will then create a new project using the command `poetry new chess-01`.
For now, there will be no need to install any external libraries or packages, but the filestructure of Poetry will help us in working out this assignment.

You will now see a structure which holds your `README.MD` file where you can explain your project, and a `chess_01` directory nested inside another one.
The deepest one has an `__init__.py` file which is used when you will be importing your project as a package. We won't be using this for now, but it is good to know.

At first, create a `main.py` file, which will be the entrypoint we use to run and start the project.

## Setting up the pieces
In the `chess_01` directory (the one that holds the `__init__.py` file), create a `pieces.py` file.

The `pieces.py` file will contain a **Base** class which is called `BaseChessPiece` and defines the functions a chess piece should be able to do:
- Move
- Can Kill (can_kill)
- Die

It does not contain an implementation of these functions yet, but it will be used as a base class for the other pieces.
Only the `die()` function should toggle the `ia_alive` property to false.
As we will be using inheritance, we will be able to use the functions of the `BaseChessPiece` class in the other pieces.
We will also be able to use the properties of the `BaseChessPiece` class in the other pieces. The properties that are used for all the pieces will be `color`, `name`, `symbol` and `position`. An `is_alive` property is also very useful to use,
The `symbol` property will be a single character, which will be used to represent the piece on the board.
The `position` property will be a tuple of two integers, which will be used to represent the position of the piece on the board, where the first integer is the position on the height of the board and the second integer is the position on the width of the board.

the `color` property can only be `BLACK` or `WHITE`. You could use an Enum for that, if you like to. I will just hardcode it as a string.

Test out your inheritance by creating a `Pawn` class that inherits from the `BaseChessPiece` and implements the `move()` function. Currently hardcode it to return a string `print("Pawn moves forward 1 position")`
Implement a test method for `can_kill` as well.

Remember that Python needs the `self` property to be added into each function. This is the way Python knows which object is calling the function.
In the `__init__()` function, we can call the constructor of the parent class by using `super().__init__()`. By passing the `color` and `identifier` property we get from the `Pawn`s constructor, we can set the properties on our base class. This way, we can use the properties of the `BaseChessPiece` class in the `Pawn` class.

Continue by setting up a `Rook` class, which can move in a straight line, and a `Bishop` class, which can move diagonally.
The `Queen` class can move in both directions of the Bishop and Rook.
The `King` class can move in all directions, but only one position at a time. It can also kill any piece that is in its way.
The `Knight` class can move in an L shape, but can only kill pieces that are in its way.

(Tip: Use GitHub Copilot to autocomplete your code, create useful comments for it to understand your code better)

## Testing the pieces

In a new `main.py` file create a `Pawn` object. this object should be imported from the `pieces.py` file using `from pieces import Pawn`. Initialize the `Pawn` object with the `color` on `BLACK` and the `identifier` on `1`. Call the `move()` function on it. Call the `can_kill()` function as well.


## Setting up the board