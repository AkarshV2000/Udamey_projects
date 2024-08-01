import random
from Udamey_art import logo_day14
from Udamey_art import data_day14
import os
def clear_console():
    os.system('cls')


game_on = True
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f" {name} , a {description} from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

account_b = random.choice(data_day14)


score = 0
while game_on :
    
    print(logo_day14[0])

    account_a = account_b
    account_b = random.choice(data_day14)
    while account_a == account_b:
        account_b = random.choice(data_day14)


    print(f"your current score is {score} ")
    print(f"Compare A: {format_data(account_a)}")
    print(logo_day14[1])
    print(f"Against B: {format_data(account_b)}")
    

    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count =  account_a['follower_count'] 
    b_followers_count =  account_b['follower_count']
        
    is_correct = check_answer(guess, a_followers_count,b_followers_count)
    
    if is_correct:
        print(f"Youre right! current score is: {score}")
        score+=1
    else:
        print(f"sorry, that's worng. Final score is: {score}")
        
        game_on = False
        clear_console()
        



