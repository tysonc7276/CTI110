# A brief description of the project
# 11/3/2020
# CTI-110 P5HW1 - Random Number
# Carlos Tyson
# This program will as you to guess a number between 1-100. If you guess wrong, it will tell you if you are too high or too low. If you guess correctly, it will say congrats! It will also record how many guesses you made in the game. 

def main():
    import random

    guesses = 1
    number = random.randint(1,100)
    guess = int(input("Guess a number between 1 and 100: "))
        
    while guess != number:
            if guess < number:
                print("Your guess is too low. Try again")
                guess = int(input("\nGuess a number between 1 and 100: "))
                guesses = guesses + 1
            elif guess > number:
                print("Your guess is too high. Try again")
                guess = int(input("\nGuess a number between 1 and 100: "))
                guesses = guesses + 1
          
      
    print("You guessed correctly! Congrats!")
    print("You made", guesses, "guesses.")
    
    while True:
        answer = input("Would you like to play again? 1 - Yes, 2 - no: ")
        if answer == '1':
            main()
        else:
            print("Goodbye")
            break
