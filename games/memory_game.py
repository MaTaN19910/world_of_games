import random
import os
import time
import numpy as np 
bool==True
## this func will generate a list of random numbers ##

def generate_sequence(game_level_input):
   lower_limit=1
   upper_limit=101
   numers_array=[0 for i in range(game_level_input)] 
   for i in range(1,game_level_input):
      numers_array[i-1] = random.randint(lower_limit,upper_limit)
   return numers_array

## this func will get the guess from user ##

def get_list_from_user(game_level_input):
   enum_list = ["First", "Second", "Third", "Fourth", "Fifth"]
   guess_input_array=[0 for i in range(game_level_input)]
   
   for i in range(1, game_level_input+1):
      bool=True
      print("Please enter the " + enum_list[i-1] + " number")  
      while bool ==True:    
         try:
            input_guess = input()
            input_guess_int = int(input_guess)
         except ValueError:
            print("wrong input please try again")
            continue
         if input_guess_int not in range(1,102):
            print("wrong input please try again")
            continue
         if i-1 == game_level_input:
            guess_input_array[i-1] =  input_guess_int
            bool = False   
         else:
            guess_input_array[i-1] =  input_guess_int
            bool = False
   return guess_input_array
   


## this func will start and manage memory game ##

def play(game_level_input):
   guess_input_array = [game_level_input]
   numers_rnd_array = [game_level_input]
   numers_rnd_array= generate_sequence(game_level_input)
   print_arr(numers_rnd_array)
   guess_input_array=get_list_from_user(game_level_input)
   is_list_equal(guess_input_array,numers_rnd_array)

## this func will determine if the player has succeded to guess the right numbers ##

def is_list_equal(guess_input_array, numers_rnd_array):
   array1 = np.array(guess_input_array)
   array2 = np.array(numers_rnd_array)
   if (array1 == array2).all():
      print("your guess is right you won!!")
   else:
      print("Your guess is wrong you lose!!")


def print_arr(numers_rnd_array):
   for i in numers_rnd_array:
      print(numers_rnd_array[i])
   time.sleep(1)
   os.system('clear')


      
      
      