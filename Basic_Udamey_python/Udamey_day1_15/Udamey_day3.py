#project1: Love Calculator . Take input of both names and calculate how many times
#letters of "TRUE" and "LOVE" occurs in the names, and combine them to print the output
#Eg: name1, name2 = maxwell, Julia

#T: 0 times     L: 3 times
#R: 0 times     O: 0 times
#U: 1 Times     V: 0 times
#E: 1 Times     E: 1 times
#Total:2        Total:4
#res = 23

name1= input("Please enter your name: ")
name2= input("Please enter your partners name: ")
new_name = name1 + name2
new_name = new_name.lower()
count = 0
t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")
first_digit = t+r+u+e
l = new_name.count("l")
o = new_name.count("o")
v = new_name.count("v")
e = new_name.count("e")
second_digit = l + o + v + e

res = int(str(first_digit) + str(second_digit))
if res >80:
    print(f" your score is {res}. It rperesnts healthy relationship")
elif res >50 and res<80:
    print(f"your socre is {res}. It represents fine reltionship")
else:
    print(f" your score is {res}.")