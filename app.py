import games.memory_game
import games.guess_game
import games.currency_roulette_game


## promt func ##

def welcome():
    print("Please enter your name:")
    name = input()
    print("Hi " + name + " and welcome to the World of Games: The Epic Journey")

## this func will present the game selections ##
def start_play():
    memory_game_starter = games.memory_game
    guess_game_starter = games.guess_game
    currency_roulette_starter = games.currency_roulette_game
    bool=False
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print("Please enter the number of the game you wish to play")
    while bool==False:    
        try:
            game = input()
            game_input=int(game)
        except ValueError:
            print("wrong input please try again")
            continue
        if game_input not in range(1,4):
                print("wrong input please try again")
        else:
            bool=True

   
    print("Please choose game level(1-5)")
    while bool==True:
        try:
            game_level = input()
            game_level_input=int(game_level)
        except ValueError:
            print("wrong input please try again")
            continue

        if game_level_input not in range(1,6):
            print("wrong input please try again")
            continue
        else:
            bool=False


## according to the player selection start the right game ##

    if game_input == 1:
        memory_game_starter.play(game_level_input)
    if game_input == 2:
        guess_game_starter.play(game_level_input)
    if game_input == 3:
        currency_roulette_starter.play(game_level_input)



        
        





             

#start play check ##
#start_play()
        

## welcome check ##
#welcome("Matan")
    
