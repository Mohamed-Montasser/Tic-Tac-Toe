# Tic-Tac-Toe Game

This repository contains a simple **Tic-Tac-Toe game** implemented in Python, where a player competes against the computer. The game is played on a 3x3 grid, and the player uses 'X' while the computer uses 'O'. The computer makes random moves, and the game checks for a winner after each move.

---

## Table of Contents
1. [Features](#features)
2. [How to Play](#how-to-play)
3. [Code Structure](#code-structure)
4. [Future Improvements](#future-improvements)

---

## Features
- **Player vs. Computer**: The player competes against a simple AI that makes random moves.
- **Interactive Gameplay**: The player inputs their move by selecting a number from 1 to 9.
- **Winning Condition Check**: The game checks for a winner after each move and displays the result.
- **Grid Display**: The current state of the grid is displayed after each move.

---

## How to Play
1. The game starts by displaying a 3x3 grid with numbers 1 to 9 representing the positions.
2. The player inputs a number (1-9) to place an 'X' in the desired position.
3. The computer then randomly places an 'O' in an available position.
4. The game checks for a winner after each move.
5. The game ends when either the player or the computer wins, or all positions are filled.

---

## Code Structure
### The code is structured into the following functions:

1. **`PrintG(listt)`**:
   - Displays the current state of the Tic-Tac-Toe grid.
   - Takes a 2D list (`listt`) as input and prints the grid in a readable format.

2. **`Set(lis1, lis2, lis3)`**:
   - Handles the player's move.
   - Prompts the player to input a number (1-9) and updates the grid with an 'X' in the chosen position.
   - Validates the input to ensure it is within the range and not already occupied.

3. **`Comp(lis1, lis2, lis3)`**:
   - Handles the computer's move.
   - Randomly selects an available position and places an 'O' there.

4. **`check(lis)`**:
   - Checks if either the player or the computer has won by examining all possible winning combinations (rows, columns, and diagonals).
   - If a winner is found, it prints the result and ends the game.

---

## Future Improvements
- **Improved AI**: Implement a smarter AI using algorithms like Minimax to make the computer more challenging.
- **GUI**: Add a graphical user interface (GUI) using libraries like `tkinter` or `pygame` for a better user experience.
- **Multiplayer Mode**: Allow two players to compete against each other.
- **Score Tracking**: Keep track of wins, losses, and draws over multiple games.
- **Input Validation**: Add more robust input validation to handle invalid inputs gracefully.
- **Save/Load Game**: Add functionality to save the game state and load it later.
