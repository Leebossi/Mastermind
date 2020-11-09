# File name: mastermind.py
# Author: Leevi Ossi
# Description: Mastermind console game

import random


# Main menu
def main_menu():
    print('''
-------------------------------------------------------------------------------
***** MASTERMIND *****
-------------------------------------------------------------------------------

a) New game
b) How to play

''')
    valid_inputs = ["a","b","A","B"]
    while True:
        try:
            command = input(":")
            if command not in valid_inputs:
                raise Exception
            break
        except:
            print("a or b only")
    return command


def rules():
    print('''
-------------------------------------------------------------------------------
rules here
blaablaa
-------------------------------------------------------------------------------
''')
    input("press Enter key to return to main menu")


# start new game by generating the code 
def start():
    code = []
    print('''
-------------------------------------------------------------------------------
starting new game
-------------------------------------------------------------------------------
''')
    for i in range(4):
        code.append(random.randrange(1,7))
    return code


# determines the difficulty
def difficulty():
    while True:
        valid_difficulty = ["E","e","M","m","E","e"]
        try:
            difficulty = str(input(":"))
            if difficulty == "e" or difficulty == "E":
                difficulty_factor = 0
            elif difficulty == "m" or difficulty == "M":
                difficulty_factor = 2
            elif difficulty == "h" or difficulty == "H":
                difficulty_factor = 4
            elif difficulty not in valid_difficulty:
                raise Exception
            break
        except:
            print("That's not a correct input")
    return difficulty_factor


# Asks user to guess the code one number at a time
def guess():

    while True:
        try:
            first_spot = int(input("First: "))
            if first_spot <= 0 or first_spot > 6:
                raise ValueError
            break
        except ValueError:
            print("Please give a number between 1-6")

    while True:
        try:
            second_spot = int(input("Second: "))
            if second_spot <= 0 or second_spot > 6:
                raise ValueError
            break
        except ValueError:
            print("Please give a number between 1-6")

    while True:
        try:
            third_spot = int(input("Third: "))
            if third_spot <= 0 or third_spot > 6:
                raise ValueError
            break
        except ValueError:
            print("Please give a number between 1-6")

    while True:
        try:
            fourth_spot = int(input("Fourth: "))
            if fourth_spot <= 0 or fourth_spot > 6:
                raise ValueError
            break
        except ValueError:
            print("Please give a number between 1-6")

    guess_code = [first_spot, second_spot, third_spot, fourth_spot]
    return guess_code

# Compares the user guess to the correct code and gives feedback
def compare(guess, code):
    black_peg = 0   # Correct color and spot
    white_peg = 0   # Correct color wrong spot
    copy_code = code.copy()
    guess_copy = guess.copy()

    # Checks the amount of black pegs
    for i in range(len(guess)):
        if guess_copy[i] == copy_code[i]:
            black_peg += 1
            copy_code[i] = 0
            guess_copy[i] = 0
   
    # Checks amount of white pegs
    for i in range(len(copy_code)):
        for x in range(len(guess)):
            if copy_code[x] == guess_copy[i] and copy_code[x] != 0:
                white_peg += 1
                copy_code[x] = 0
                guess_copy[i] = 0
                
    return black_peg, white_peg


game = 1
feed_list = []
turns = 0
command = main_menu()
while command != "a" and command != "A":
    if command == "b" or command == "B":
        rules()
        command = main_menu()
correct_code = start()

print('''
Please choose difficulty
(e)asy, (m)edium, (h)ard
''')
difficulty_factor = difficulty()  
turns = turns + difficulty_factor
print('''
-------------------------------------------------------------------------------
''')

#print("Correct code",code) # for testing

while game == 1:
    user_code = guess()
    result = compare(user_code, correct_code)
    code_to_string = ' '.join([str(elem) for elem in user_code])
    result_to_str = ' '.join([str(elem) for elem in result])
    correct_code_to_string = ' '.join([str(elem) for elem in correct_code])
    feed = code_to_string + "  *  " + result_to_str
    feed_list.append(feed)
    print('''
-------------------------------------------------------------------------------
''')
    print("C O D E     B W")
    print("\n".join(feed_list))
    print('''
-------------------------------------------------------------------------------
''')
    turns += 1
    if user_code == correct_code:
        game = 2
    elif turns > 11:
        game = 0

if game == 2:
    print('''
-------------------------------------------------------------------------------
Congratulations, you've won!
-------------------------------------------------------------------------------
''')

elif game == 0:
    print('''
-------------------------------------------------------------------------------
You have reached maximum amount of guesses. \nThe correct code is:
''',correct_code_to_string, '''\nYou lose!
-------------------------------------------------------------------------------
''')
    
    


    
