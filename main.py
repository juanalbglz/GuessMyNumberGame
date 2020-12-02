from replit import clear
import random

#Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
NUMBER = random.randint(0, 100)

#Global variables
logo = '''
                                                                     _               
                                                                    | |              
  __ _ _   _  ___  ___ ___   _ __ ___  _   _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | '_ ` _ \| | | | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | | | | | | |_| | | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/ |_| |_| |_|\__, | |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
  __/ |                                 __/ |                                        
 |___/                                 |___/                                         

'''

#Auxiliar functions


#Game level selector
def game_level():
    level = input("Choose a difficulty. Tipe 'h' for HARD or 'e' for EASY: ")
    while level != 'h' and level != 'e':
        level = input(
            "I din not undestood your answer \nChoose a difficulty. Type 'h' for HARD or 'e' for EASY: "
        )
    if level == 'e':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


#Comaper guess if not equal and give hint
def hint_guess(guess):
    if guess > NUMBER:
        print("Too high.")
    elif guess < NUMBER:
        print("Too low.")


def guess_it(turns):
    guess = int(input("Make a guess: "))
    if guess != NUMBER:
        hint_guess(guess)
        turns = turn_over(turns)
    else:
        print(f"You guessed the number {NUMBER}!")
        quit()
    return turns


#track turns
def turn_over(turns):
    print(f"You have {turns} attemps remaining to guess the number")
    return turns


#game function
def guess_game():
    clear()
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    turns = game_level()
    while turns > 0:
        turns = guess_it(turns)


guess_game()
