# #randomizaton in python
# import random #imprt the random module

# #program for head and tails

# res = random.randint(0,1)
# if res == 0: print("Tails")
# if res == 1: print("Heads")

# # there are many different functions present in import module, make sure to check them out


##   ROCK , PAPER AND SISSOR GAME ##

import random
rock = "ROCK"
paper = "PAPER"
scissor = "SCISSOR"

n = int(input(" Choose 0 for rock or 1 for paper or 2 for sissors "))
i = random.randint(0,2)

if n == 0:
    print(f"User has choosen {rock}")
    if i == 0:
        print(f" Computer has choosen {rock}, it's a draw")
    if i == 1:
        print(f" Computer has choosen {paper}, you loose")
    if i == 2:
        print(f" Computer has choosen {scissor}, you WIN!!")

if n == 1:  
    print(f"User has choosen {paper}") 
    if i == 0:
       print(f" Computer has choosen {rock}, you WIN!!")
    if i ==1:
        print(f" Computer has choosen {paper}, it's a draw")
    if i == 2:
        print(f" Computer has choosen {scissor}, you loose")

if n == 2:
    print(f"User has choosen {scissor}") 
    if i == 0:
        print(f" Computer has choosen {rock}, you loose")
    if i == 1:
        print(f" Computer has choosen {paper}, you WIN!!")
    if i == 2:
        print(f" Computer has choosen {scissor}, it's a draw")
if n>2:
    print ("Inpur isout of range, please select proper input")






       
       


