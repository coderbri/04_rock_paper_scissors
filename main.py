import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to a game of Rock Paper Scissors!")

user_choice = int(input("What do you choose? Type:\n - 0 for Rock,\n - 1 for Paper and\n - 2 for Scissors.\n"))

# Validate user input before accessing the list
if user_choice >= 3 or user_choice < 0:
    print("Invalid Input. Game Over.")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # WIN if... scissors, beat paper -> if paper, beat rock -> if rock, beat scissors
    if user_choice == 0 and computer_choice == 2:
        print("You win!")                   # User: rock > scissors
    elif computer_choice == 0 and user_choice == 2:
        print("You lose. Game Over.")       # Computer: rock > scissors
    elif user_choice > computer_choice:
        print("You win!")                   # User: 2 > 1 > 0
    elif computer_choice > user_choice:
        print("You lose. Game Over.")       # Computer: 2 > 1 > 0
    elif user_choice == computer_choice:
        print("It's a draw!")               # TIE
