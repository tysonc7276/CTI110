# A brief description of the project
    # 11/04/2020
    # CTI-110 P5HW2 - Math Quiz
    # Carlos Tyspm
    # Program creates a random addition or subtraction quiz, based off of user's
    # choice. The user will answer the question. If the answer is incorrect, the
    # user will continue to answer the question until it's correct. Once the
    # answer is correct, the user will return to the menu and select addition or
    # subtraction. If user selects 3, the quiz will end.

import random

def display_intro():
    title = "Math Quiz Main Menu" 
    print(title)
    
def display_menu():
    menu_list = ["1. Add Random Numbers", "2. Subtract Random Numbers", "3. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 3 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again 1, 2, or 3: "))
    else:
        return user_input

def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

def check_solution(user_solution, solution):
    if user_solution == solution:
        print("Correct.")
    else:
        print("Incorrect.")

def menu_option(index):
    number_one = random.randint(1, 300)
    number_two = random.randint(1, 300)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        while user_solution != solution:
            if user_solution < solution:
                print("Your guess is too low. Try again")
                user_solution = get_user_solution(problem)
            elif user_solution > solution:
                print("Your guess is too high. Try again")
                user_solution = get_user_solution(problem)
        print("That's the correct answer! Good Job")
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        while user_solution != solution:
            if user_solution < solution:
                print("Your guess is too low. Try again")
                user_solution = get_user_solution(problem)
            elif user_solution > solution:
                print("Your guess is too high. Try again")
                user_solution = get_user_solution(problem)
        print("That's the correct answer! Good Job")
    
    
def main():
    display_intro()
    display_menu()

    option = get_user_input()
    
    while option != 3:
        correct = menu_option(option)
        option = get_user_input()
    while option == 3:
        print("Thank you for playing! See you next time!")
        break

main()

    
