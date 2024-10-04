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

# Accept user choice
print("Welcome to the Rock, Paper, Scissors game!")
user_choice = int(input("Please choose from the below options:\n0---->Rock\n1---->Paper\n2---->Scissors\n"))

# Generating computer selection
computer_choice_int = random.randint(0,2)

# Printing user selection
if user_choice == 0:
    print("Your choice is Rock\n" + rock)
    # Computer choice printing
    if computer_choice_int == 0:
        print("The computer chose Rock\n" + rock)
    elif computer_choice_int == 1:
        print("The computer chose Paper\n" + paper)
    else:
        print("The computer chose Scissors\n" + scissors)
    # Result calculating
    if computer_choice_int == 2:
        print("You win!")
    elif computer_choice_int == 1:
        print("You lose!")
    else:
        print("Match Drawn!")
elif user_choice == 1:
    print("Your choice is Paper\n" + paper)
    # Computer choice printing
    if computer_choice_int == 0:
        print("The computer chose Rock\n" + rock)
    elif computer_choice_int == 1:
        print("The computer chose Paper\n" + paper)
    else:
        print("The computer chose Scissors\n" + scissors)
    # Result calculating
    if computer_choice_int == 0:
        print("You win!")
    elif computer_choice_int == 2:
        print("You lose!")
    else:
        print("Match drawn!")
elif user_choice == 2:
    print("Your choice is Scissors\n" + scissors)
    # Computer choice printing
    if computer_choice_int == 0:
        print("The computer chose Rock\n" + rock)
    elif computer_choice_int == 1:
        print("The computer chose Paper\n" + paper)
    else:
        print("The computer chose Scissors\n" + scissors)
    # Result calculating
    if computer_choice_int == 1:
        print("You win!")
    elif computer_choice_int == 0:
        print("You lose!")
    else:
        print("Match drawn!")
else:
    print("Wrong choice. You lose!")

