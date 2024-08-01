#f-strings are used to concatinate different data  types in a single line of code


#program to check how many weeks are left for the user until he's turnng 90
#we will assume that user is going to live 90 years(4000 weeks)
#we going to take age of the user as input and give output as reamining weeks

# age = int(input("What's your current age? "))
# total_week = age*54
# remaining_week = 4000 - total_week
# print(f"Total week remining are {remaining_week}")



#Program to calculate tip
#We will take input of total bill from users
#we will give then three choices for the total percentage of the tip
#we will take input of the total numbers of ppls they want to split
#we will return them final result of splitted bill upto two decimal point value


total_bill = float(input("Please enter the total bill? "))
total_tip = int(input ("total amout of percentage of tip you'd like to give 10, 12 or 15: "))
final_bill = ((total_bill * total_tip)/100)
split_number= int(input("How many ppls you'd like to split the bill? "))
res = round(total_bill/split_number,2)
print(f"Each person should pay: {res}")





