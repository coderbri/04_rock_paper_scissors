# 04 Rock Paper Scissors

This is the **Day 4 Challenge** from Dr. Angela Yu's 100 Days of Code: Python Pro Bootcamp. This project implements a classic game of Rock Paper Scissors, showcasing the following Python concepts:
- Random Module
- Understanding Offset and Appending Items to Lists
- Handling IndexErrors
- Working with Nested Lists

## Project Description

In this project, you can play a simple game of Rock Paper Scissors against the computer. The program generates random choices for the computer and evaluates the outcome based on the user’s input. The game uses ASCII art to represent each choice (rock, paper, or scissors).

## How It Works

1. The user is prompted to choose Rock (0), Paper (1), or Scissors (2).
2. The computer randomly selects its own choice using the `random.randint()` function.
3. The program then compares the choices to determine the winner using conditional statements.
4. The outcome (win, lose, or draw) is printed, along with the corresponding ASCII art for both the user’s and computer’s choices.

### Example

```
Welcome to a game of Rock Paper Scissors!
What do you choose? Type:
 - 0 for Rock,
 - 1 for Paper and
 - 2 for Scissors.

You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You lose.
```

## How to Run

1. Clone this repository or download the `main.py` file.
2. Run the script with Python 3:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts to play the game.

---

<section align="center">
  <code>coderBri © 2024</code>
</section>
