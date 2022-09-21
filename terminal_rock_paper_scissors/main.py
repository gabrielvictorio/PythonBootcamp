#!/usr/bin/env python3
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
import random 
print("Welcome to the Rock Paper Scissors game!\n")
choice = int(input("Select 1 for rock, 2 for paper ande 3 for scissors! \n"))

if choice > 3 or choice <1 :
  print( "INVALID NUMBER, YOU LOSE!")
else:
  if choice == 1:
    print(rock)
  elif choice == 2:
    print(paper)
  else:
    print (scissors)

  print("The Computer chose ")

  computer_choices = [rock, paper, scissors]
  final_choice = random.choice(computer_choices)

  print(final_choice)

  #Rock wins against scissors.
  #Scissors win against paper.
  #Paper wins against rock.


  if final_choice == "rock":
    if choice == 1:
      print ("It's a tie!")
    elif choice == 2:
      print("You lost")
    else: 
      print ("You win!")
  elif final_choice == "paper":
    if choice == 1:
      print ("You win!")
    elif choice == 2:
      print("It's a tie!")
    else: 
      print ("You lost!")
  else :
    if choice == 1:
      print ("You lost")
    elif choice == 2:
      print("You win!")
    else: 
      print ("It's a tie!")


