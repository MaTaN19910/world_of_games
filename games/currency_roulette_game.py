#from forex_python.converter import CurrencyRates
import random
import requests
from score import add_score

## this func will convert usd to current ils by the up to date rate ##
def usd_to_ils_convertor():
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/4fb8d36deda0bec7b0dea75d/latest/USD'

    # Making our request
    response = requests.get(url)
    
    data = response.json()

    # Your JSON object
    return data['conversion_rates']['ILS']


## this func will prompt a guess to the user ##
def get_guess_from_user():
    bool=True
    print("Please enter you guess number")
    while bool==True:
        try:    
            input_guess = input()
            input_guess_int = int(input_guess)
        except ValueError:
            print("wrong input please try again")
            continue
        else:
            bool=False
    return input_guess_int

## this func will generate a random number ##
def generate_random_number():
    lower_limit=1
    upper_limit=101
    random_number = random.randint(lower_limit,upper_limit)
    return random_number

"""
this func will get a random number 
and according to the usd to ils rate 
and the diffrence will calc the winning numbers by range
"""

def get_money_interval(game_level_input):
    global upper, lower
    random_num = generate_random_number()
    usd_to_ils = usd_to_ils_convertor()
    diffrence = 10 - game_level_input
    upper = random_num*usd_to_ils + diffrence
    lower = random_num*usd_to_ils - diffrence

"""
this func will compere the results and declare the winner
"""
def compare_results(input_guess):
    if input_guess == upper:
        print("your guess is right you won!!")
    if lower > 0 and input_guess == lower:
        print("your guess is right you won!!")
        add_score()
    else:
        print("Your guess is wrong you lose")



## this gunc will oprate the game funcs ##

def play(game_level_input):
    get_money_interval(game_level_input)
    input_guess = get_guess_from_user()
    compare_results(input_guess)


