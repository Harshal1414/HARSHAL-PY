# EXERCISE 3

n = 56
number_of_guesses=1

print("This is a number guessing game.")

while(number_of_guesses<=6):
    Guess=int(input("Guess a number between 1 to 100:, and number of guesses are limited upto 6 times\n"))
    if Guess<56:
        print("it is lesser\n")
    elif Guess>56:
        print("It is greater\n")
    else:
        print("Congrats! You got it\n")
        print(number_of_guesses,"No. of guesses you took to finish.")
        break
    print(6-number_of_guesses,"NO. of guesses left.")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>6):
    print("Game over") 