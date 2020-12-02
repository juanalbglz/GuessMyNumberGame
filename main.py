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

#evaluate game conditions
def check_game_conditions(guess):
    if guess > NUMBER:
        print("Too high.")
    elif guess < NUMBER:
        print("Too low.")
    else:
        print(f"You found the number {NUMBER}")
        return NUMBER

#game_turn 
def game_turn(attemps):
    print(f"You have {attemps} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if check_game_conditions(guess) == NUMBER:
        return NUMBER
    else:
        attemps -= 1
        game_turn(attemps)

#game function
def guess_game():
    clear()
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    attemps = game_level()
    game_turn(attemps)
        

    if input("Play again ('y' or 'n'): ") == 'y':
        guess_game()

guess_game()
