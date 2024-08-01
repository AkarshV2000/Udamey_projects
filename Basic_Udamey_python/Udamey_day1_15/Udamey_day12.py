###################  SCOPE  ###################

# There are two types of scope, Local Scope aand Gobal Scope

# def odd():
#     odd_number = 3  
#     ''' Variables which are defined inside a function are known as 
#         Local variables/Scope, we cannot use them outside the function itself
#          If we try to call them outside the function it'll give out an error'''
#     print(odd_number)

# even_number = 4
# ''' Variables which are defined ouside are known as 
#     Global variables/Scope, we can use them inside any function or anywhere'''

# enemies = 2 #Global Variable
# def game():
#     enemies = 1 # Local Variable
#     print(f"Total enimies inside are: {enemies}") #output 1
#     '''in this particular case single variable enemies is used on both
#         inside as well as outside the function. But the variable defined inside
#         the function is totally different from the variable outside, even though
#         there names are same but program will treat them as totally different ones
#         , You can modify as much as you want the inside variable, it's value will
#         always stay inside the funtion bc it's a toatally different variable'''

# print(f"Total enemies outside are: {enemies} ") #output 2


####### Guess the Number #############
import random
import os
def clear_console():
    os.system('cls')
res = random.randint(1,100)


def start_game():
    level = input(" pick the level 'easy' or 'hard': ")
    chances = 0
    if level  == "easy":
        chances = 10
    else:
        chances = 5


    while chances !=0:
        guess = int(input(f" guess a number bw 1 to 100 you have {chances} number of chances: "))
        if guess > res:
            chances -=1
            print(f" Too High")
        elif guess < res:
            chances -=1
            print(f" Too Low")
        else:
            print(f"{guess} is the correct number")
            break
    if chances == 0:
        print("Game Over, you were not able to guess")

print("Welcome tonumber guessing game!")
print("I,m thinking of a number between 1 to 100")
start_game()
clear_console()


        

