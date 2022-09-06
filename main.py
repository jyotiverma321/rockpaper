rock = '''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
available_choice = ["Rock","Paper","Scissor"]
game_images = [rock, paper, scissors]
my_turn = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." ))

print("You choose", game_images[my_turn])

iter_number = len(available_choice)
comp_turn_value = random.randint(0,iter_number-1)

my_turn_value = int(my_turn)

comp_turn_value = random.randint(0,2)
# comp_turn_value = comp_turn

# comp_turn_value = random.choice(available_choice)
print("Computer choose", game_images[comp_turn_value])


# print(game_images[c0omp_turn_value])
# if comp_turn_value == "Rock" and my_turn=="Rock":
#   print("Its a tie")
# elif comp_turn_value == "Rock" and my_turn == "Paper":
#   print("computer win")
# elif comp_turn_value == "Rock" and my_turn == "Scissor":
#   print("Computer win")
# elif comp_turn_value == "Paper" and my_turn == "Rock":
#   print("You win")
# elif comp_turn_value == "Paper" and my_turn == "Paper":
#   print("Its a tie")
# elif comp_turn_value == "Paper" and my_turn == "Scissor":
#   print("You Win")
# elif comp_turn_value == "Scissor" and my_turn == "Rock":
#   print("You Win")
# elif comp_turn_value == "Scissor" and my_turn == "Paper":
#   print("computer win!")
# elif comp_turn_value == "Scissor" and my_turn == "Scissor":
#   print("Its Tie")

if comp_turn_value == 0 and my_turn_value == 0:
  print("Its a tie")
elif comp_turn_value == 0 and my_turn_value == 1:
  print("computer win")
elif comp_turn_value == 0 and my_turn_value == 2:
  print("You win")
elif comp_turn_value == 1 and my_turn_value == 0:
  print("You win")
elif comp_turn_value == 1 and my_turn_value == 1:
  print("Its a tie")
elif comp_turn_value == 1 and my_turn_value == 2:
  print("You Win")
elif comp_turn_value == 2 and my_turn_value == 0:
  print("You Win")
elif comp_turn_value == 2 and my_turn_value == 1:
  print("computer win")
elif comp_turn_value == 2 and my_turn_value == 2:
  print("Its Tie")
else:
  print("Invalid number")