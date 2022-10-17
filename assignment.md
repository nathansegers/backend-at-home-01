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
Only the `die()` function should toggle the `is_alive` property to false.
As we will be using inheritance, we will be able to use the functions of the `BaseChessPiece` class in the other pieces.
We will also be able to use the properties of the `BaseChessPiece` class in the other pieces. The properties that are used for all the pieces will be `color`, `name`, `symbol` and `position`. An `is_alive` property is also very useful to use,
The `symbol` property will be a single character, which will be used to represent the piece on the board.
The `position` property will be the name of the position on the board. This could be `A3` or `H6` for example. This will be calculated when the board is attached in the next steps of this project. 

the `color` property can only be `BLACK` or `WHITE`. You could use an Enum for that, if you like to. I will just hardcode it as a string (for now)

Test out your inheritance by creating a `Pawn` class that inherits from the `BaseChessPiece` and implements the `move()` function. Currently hardcode it to return a string `print("Pawn moves forward 1 position")`. Later on, we will implement the actual movement
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

In the `chess_01` directory, create a `board.py` file.
In the file, we will create a `Board()` class. The constructor (`__init__()`) method of this function, we use a dict comprehension to create a dictionary of `squares` (use `squares` as the property name). The keys are the square names and the values are None.
You can use the `range(ord('a'), ord('i'))` to create a range for the alphabetical characters and `range(1, 9)` to create a range for the numbers.
Those represent the rows and columns of the chess board.
The alphabetical characters are the columns, whereas the numerical characters are the rows.
The result will look like this:
```python
{'a1': None, 'a2': None, 'a3': None, 'a4': None, 'a5': None, 'a6': None, 'a7': None, 'a8': None, 'b1': None, 'b2': None, 'b3': None, 'b4': None, 'b5': None, 'b6': None, 'b7': None, 'b8': None, 'c1': None, 'c2': None, 'c3': None, 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'd1': None, 'd2': None, 'd3': None, 'd4': None, 'd5': None, 'd6': None, 'd7': None, 'd8': None, 'e1': None, 'e2': None, 'e3': None, 'e4': None, 'e5': None, 'e6': None, 'e7': None, 'e8': None, 'f1': None, 'f2': None, 'f3': None, 'f4': None, 'f5': None, 'f6': None, 'f7': None, 'f8': None, 'g1': None, 'g2': None, 'g3': None, 'g4': None, 'g5': None, 'g6': None, 'g7': None, 'g8': None, 'h1': None, 'h2': None, 'h3': None, 'h4': None, 'h5': None, 'h6': None, 'h7': None, 'h8': None}
```

Use GitHub Copilot to autocomplete the code to fill in the chess pieces on the right order.
You can do this in a function called `setup_board` which will be called in the constructor of the `Board` class.

### Creating some more helper functions into the board

A few functions we can use in the `Board` class are:

#### `setup_board()`
`setup_board()` will add all the pieces to the board using the `squares` property.
This will be done using the piece classes we created earlier on. Take a look at this example:
```python
from pieces import Rook, Knight
self.squares['a1'] = Rook('BLACK', 1) # This defines the first Rook of the BLACK team.
self.squares['b1'] = Knight('BLACK', 1) # This defines the first Knight of the BLACK team.

# Use a dict comprehension to add the black pawns on row 2, the keys are the square names and the values are the pieces.
# Update the black pawns to the squares property
# Repeat for the white pawns, they are on rows 7
```
#### `print_board()`
Will print all the rows of the board in a row-first way.
This will represent the board in a different way than the default dictionary way.
The result should look like this:
```
[BLACK Rook 1, BLACK Knight 1, BLACK Bishop 1, BLACK Queen 1, BLACK King 1, BLACK Bishop 2, BLACK Knight 2, BLACK Rook 2]
[BLACK Pawn 1, BLACK Pawn 2, BLACK Pawn 3, BLACK Pawn 4, BLACK Pawn 5, BLACK Pawn 6, BLACK Pawn 7, BLACK Pawn 8]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[WHITE Pawn 1, WHITE Pawn 2, WHITE Pawn 3, WHITE Pawn 4, WHITE Pawn 5, WHITE Pawn 6, WHITE Pawn 7, WHITE Pawn 8]
[WHITE Rook 1, WHITE Knight 1, WHITE Bishop 1, WHITE Queen 1, WHITE King 1, WHITE Bishop 2, WHITE Knight 2, WHITE Rook 2]
```

You can achieve this by looping over the 8 rows, starting with row `1` if the key name ends with `1`. If you nest this in a list, using the **list comprehensions** syntax, you can loop over them later and print everything.

#### `find_piece(symbol, identifier, color)`
Use a dict comprehension to loop over all the `self.squares.items()` and return those where the `symbol`, `identifier` and `color` are the same.

Use these scripts as well, they might come in handy later

```python
def get_piece(self, square):
    """Returns the piece that is on a specific square"""
    return self.squares[square]

def is_square_empty(self, square):
    """Returns True if the square is empty, False otherwise."""
    return self.get_piece(square) is None
```

#### `kill_piece(square)`
This method should be called to kill a certain piece on a certain square.
Functions that check if the killing is allowed is happened before this one is executed.