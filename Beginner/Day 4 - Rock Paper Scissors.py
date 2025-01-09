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
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

l=[rock,paper,scissors]

import random
computer_choice=random.randint(0,2)

user_choice=int(input('''Rock, Paper, or Scissors?
What Do You Choose?
Type 0 for Rock, 1 for Paper, and 2 for scissors'''))

print(f"You Chose {l[user_choice]}")
print(f"Computer Chose {l[computer_choice]}")

x=user_choice
y=computer_choice

if x==0:
    if y==0:
        print("You Both Chose The Same! It's a Draw!!")
    elif y==1:
        print("Unfortunately, You Lose!!")
    else:
        print("Congratulations! You Win!!")
elif x==1:
    if y==0:
        print("Congratulations! You Win!!")
    elif y==1:
        print("You Both Chose The Same! It's a Draw!!")
    else:
        print("Unfortunately, You Lose!!")
else:
    if y==0:
        print("Unfortunately, You Lose!!")
    elif y==1:
        print("Congratulations! You Win!!")
    else:
        print("You Both Chose The Same! It's a Draw!!")



