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

    print('''Please choose a game to play:
          1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
          2. Guess Game - guess a number and see if you chose like the computer.
          3. Currency Roulette - try and guess the value of a random amount of USD in ILS
          Please enter the number of the game you wish to play''')
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
        rematch()
    if game_input == 2:
        guess_game_starter.play(game_level_input)
        rematch()
    if game_input == 3:
        currency_roulette_starter.play(game_level_input)
        rematch()



        
def rematch():
    end_game = False
    print("""If you wish to play again please press yes, if you wish to end press no""")
    while end_game == False:
            game = input()
            if game != 'yes' and game != 'no':
                print("Wrong input please try again")
            else:
                end_game=True
    if game == 'yes':
        start_play()
    else:
        print("Thanks for playing world of games")

def new_func():
    return False





             

#start play check ##
#start_play()
        

## welcome check ##
#welcome("Matan")
    
