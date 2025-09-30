import random

# ASCII art
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

options = [rock, paper, scissors]
user_choice = int(input("What do you want to choose: 0 for rock, 1 for paper or 2 for scissors"))

if user_choice >= 3 and user_choice <= 0:
    print("You chose an invalid number. You lose😕")
else:
    print("You choose:")
    print(options[user_choice])
# Computer choice
computer_choice = (random.randint(0, 2))
print("Computer Chose:")
print(options[computer_choice])

#Game logic
if user_choice == computer_choice:
    print("Its a Draw")
elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
    print("You Win 🤑")
else:
    print("You Lose☹️")

