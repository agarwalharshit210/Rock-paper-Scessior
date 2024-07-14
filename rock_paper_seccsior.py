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

guess_name = [rock,paper,scissors]
user_choice = int(input("Enter choice \n0. Rock\n1.Paper\n2.Scissors\n"))
print(guess_name[user_choice])

computer_choice = random.randint(0,2)
print(guess_name[computer_choice])

if user_choice>=3 and user_choice<0:
    print("enter valid number")
elif user_choice == 0 and computer_choice==2:
    print(computer_choice,user_choice,"You Win")
elif computer_choice==0 and user_choice==2:
    print(computer_choice,user_choice,"You Lose")   
elif user_choice>computer_choice:
    print(computer_choice,user_choice,"You Win")   
elif computer_choice>user_choice:
    print(computer_choice,user_choice,"You Lose")
elif computer_choice == user_choice:
    print(computer_choice,user_choice,"Draw")    

print()    
