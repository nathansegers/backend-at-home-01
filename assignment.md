# Assignment 1 -- Extensive Python Functionalities

## Introduction

This assignment will guide you through using the different Python functionalities the Theory class was about.
This goes through Inheritance in Python, so you learn about Object Oriented Programming.
By using Decorators, List and Dict comprehensions and Generartors, combined with the knowledge of Inheritance, you will be able to create a simple project.

## Assignment explanation

The assignment is about creating a simple game.
We will create a chess game, but only a textual representation in the dictionary states.
Later on, we can re-use this project in some of our other classes.

## Getting started

Make sure you install Poetry using the help in the theory class.
We will then create a new project using the command `poetry new chess-01`.
For now, there will be no need to install any external libraries or packages, but the filestructure of Poetry will help us in working out this assignment.

You will now see a structure which holds your `README.MD` file where you can explain your project, and a `chess_01` directory nested inside another one.
The deepest one has an `__init__.py` file which is used when you will be importing your project as a package. We won't be using this for now, but it is good to know.

## Setting up the folder structure
At first, create a `main.py` file, which will be the entrypoint we use to run and start the project.
In the `chess_01` directory (the one that holds the `__init__.py` file), create a `Pieces` directory, which will also need an empty `__init__.py` file.