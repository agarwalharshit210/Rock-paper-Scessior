import random

def Game():

    while True:
        guess_name = ["rock","paper","scissors"]
        user_choice = int(input("Enter choice \n0. Rock\n1.Paper\n2.Scissors\n"))

        computer_choice = random.randint(0,2)

        if user_choice>=3 or user_choice<0:
            print("enter valid number")
            userin = input("You want to play more (Yes/No) ")
            if userin.lower() == 'yes':
                pass
            else:
              print("Thank you")
              break 
        elif user_choice == 0 and computer_choice==2:
            print(f"You choice : {guess_name[user_choice]}")
            print(f"Computer choice : {guess_name[computer_choice]}")
            print("You Win")
            userin = input("You want to play more (Yes/No) ")
            if userin.lower() == 'yes':
                pass
            else:
              print("Thank you")
              break 
        elif computer_choice==0 and user_choice==2:
            print(f"You choice : {guess_name[user_choice]}")
            print(f"Computer choice : {guess_name[computer_choice]}")
            print("You Lose") 
            userin = input("You want to play more (Yes/No) ")
            if userin.lower() == 'yes':
                pass
            else:
              print("Thank you")
              break   
        elif user_choice>computer_choice:
            print(f"You choice : {guess_name[user_choice]}")
            print(f"Computer choice : {guess_name[computer_choice]}")
            print("You Win")  
            userin = input("You want to play more (Yes/No) ")
            if userin.lower() == 'yes':
                pass
            else:
               print("Thank you")
               break  
        elif computer_choice>user_choice:
            print(f"You choice : {guess_name[user_choice]}")
            print(f"Computer choice : {guess_name[computer_choice]}")
            print("You Lose")
            userin = input("You want to play more (Yes/No) ")
            if userin.lower() == 'yes':
                pass
            else:
               print("Thank you")
               break   
        elif computer_choice == user_choice:
            print(f"You choice : {guess_name[user_choice]}")
            print(f"Computer choice : {guess_name[computer_choice]}")
            print("Draw")  
            userin = input("You want to play more (Yes/No) ")
            if userin.lower() == 'yes':
                pass
            else:
               print("Thank you")
               break       

        print()    

if __name__ == '__main__':
    Game()
