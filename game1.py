"""This is going to be a simple guessing game
where the computer will generate a random number between 1 to 10,
and the user has to guess it in 5 attempts."""


def game(player_name,num):

    print("Okay! " + player_name + " I am choosing a number and you will guess it.")
    no_of_guess = 0
    while no_of_guess<5:
        try:
            guess = int(input())
            no_of_guess +=1
            if guess<num:
                print("Your guess is too low.")
            elif guess>num:
                print("Your guess is too high.")
            else:
                print("You guessed the number in " + str(no_of_guess) + " tries!")
                break
        except ValueError:
            print("Please enter a number!!")

    if no_of_guess >=5:
        print("Alas! You finished all your attempts in vain. The chosen number was " + str(num) + ".")

    print("Do you want to play again? Enter 1 for Yes and 0 for No.")
    reply = int(input())
    return reply
        

import random
num = random.randint(1,10)
player_name = input("Hello, What's your name?    ")  
result = int(game(player_name,num))
while result == 1:
    num = random.randint(1,10)
    result = int(game(player_name,num))
print("End Game!!!")