#Math Quiz
#11/29/2022
#CTI-110 P5HW2 - Math Quiz
#Susanna Quayle
#


#import random number generator
import random

guess = 0
count = 1
user_select = 0

#define functions
def adding_numbers(num1, num2):
    sumNums = num1 + num2
    print(num1)
    print("+" , num2)
    print()
    print("Enter answer.")
    guess = int(input())
    count = 1
    while guess != sumNums:
       if guess > sumNums:
            print("Sorry, guess is too high.")
       elif guess < sumNums:
            print("Sorry, guess is too low.")
       count+=1
       print("Try again: ", end="")
       guess = int(input())
    else:
        print("Congratulations!!! Your answer is correct!")
        print("Number of guesses:", count)
        print()


def subtracting_numbers(num1, num2):
    solve = num1 - num2
    print(num1)
    print("-" , num2)
    print()
    print("Enter answer.")
    guess = int(input())
    count = 1
    while guess != solve:
        if guess > solve:
            print("Sorry, guess is too high.")
        elif guess < solve:
            print("Sorry, guess is too low.")
        count+=1
        print("Try again: ", end="")
        guess = int(input())
    else:
        print("Congratulations!!! Your answer is correct!")
        print("Number of guesses:", count)
        print()

#print Math Quiz and Main Menu
while user_select != '3':
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"Welcome to Math Quiz")
    print()
    print(f"MAIN MENU")
    print(f'{"-"*50}')
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

    #user select option
    print("Please choose one of the menu options: ", end="")
    user_select = input()
    print()

    #call functions based on user selection
    if user_select == '1':
        adding_numbers(num1, num2)
    elif user_select == '2':
        subtracting_numbers(num1, num2)
    elif user_select == '3':
        print("Thank you for playing...")
        print("Bye!!")
    else:
        print("Invalid option")
        print()




