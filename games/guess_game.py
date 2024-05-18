import random

import numpy as np 

## game starter ##
def play(game_level_input):
    random_number=generate_number(game_level_input)
    input_guess_int=get_guess_from_user(game_level_input)
    compare_results(random_number, input_guess_int)

## generate a random number by range ##
def generate_number(game_level_input):
    lower_limit=0
    upper_limit=game_level_input
    random_number = random.randint(lower_limit,upper_limit)
    return random_number

## this func will prompt the user for a number ##
def get_guess_from_user(game_level_input):
    bool=True
    print("Please enter you guess number")
    while bool==True:
        try:    
            input_guess = input()
            input_guess_int = int(input_guess)
        except ValueError:
            print("wrong input please try again")
            continue
        if input_guess_int not in range(0,game_level_input+1):
            print("wrong input please try again")
            continue
        else:
            bool=False
    return input_guess_int

## this func will compare the results and declare the winner!! ##
def compare_results(random_number, input_guess_int):
    if random_number == input_guess_int:
        print("your guess is right you won!!")
    else:
        print("Your guess is wrong you lose!!")

