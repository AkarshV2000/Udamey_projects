# Basic stuff about forr loop and all, which i already now, 
# Just one thing whic i havent used much in for loop is the use of "Step"


# in code below we are looping fromrange 1 to 100 whle the step count is 3,
# which basically means after appending i it will skip thenext 3 values before appending again.
# res = []
# for i in range(1, 100,3):
#     res.append(i)
# print(res)


##    " FizzBuzz Game"
# ez game, take a number ranging from 1 to 100, and if thenumber is divisible
# by 3 type "Fizz" oe if the the nmber is divisble by 5, wite "Buzz"
# and if the number is divisible by both type " FizzBuzz"

# target = 100
# for i in range(1, target+1):
#     if i %3 == 0 and i %5 == 0:
#         print("FizzBuzz")
#     elif i% 3 == 0:
#         print("Fizz")
#     elif i% 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



##    Strong Password ##

import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                 'u', 'v', 'w', 'x', 'y', 'z' ,'A', 'B', 'C', 'D', 'E', 
                 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

m = int(input(" How many leters you need : "))
n= int(input("how many speial characters you need: "))
o = int(input(" how many numbers you need: "))
res = []
for i in range(1, m+1):
    res.append(random.choice(letters_list))
for i in range(1, n+1):
    res.append(random.choice(special_characters))
for i in range(1, o+1):
    res.append(random.choice(numbers_list))
random.shuffle(res)

pswd = ""
pswd = ''.join(res)
# for char in res:
#     pswd+=char
print(f" Your password is:{pswd}")











