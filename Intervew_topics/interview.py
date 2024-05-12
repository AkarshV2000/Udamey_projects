
## QUESTIONS ON STRINGS

#  --> Reverse "vikas"     ###########

# s = "vikas"
# res = ""
# for i in s[::-1]:
#     res+=i
# print(res)

 

# --> Reverse word "vikash" in sentence           ##########

# sentence="hai this is vikas  vikash haivikash haithisisisvikash vikash hivikashismyname"
# modified_sentence = sentence.replace("vikash", "hsakiv")
# print(modified_sentence)


#---> Question on valid Anagram                    ##############


## METHOD 1   -  Basically Brute Force

# s = "anagram"
# t = "nagaram"
# s_list = list(s)
# t_list = list(t)
# s_list.sort()
# t_list.sort()


# if len(s_list) == len(t_list):
#     count = 0
#     for i in range(0,len(s_list)):
#         count+=1
#         if s_list[i]!= t_list[i]:
#             print("invalid anagram")
#             break
#         else:
#             continue
#     if count == len(s_list):
#         print("valid anagram")
# else:
#     print("invalid anagram")


## METHOD 2   : Use of Function looks bit more optimised and neat

# def valid_anagram(str1,str2):
#     s_list = list(str1)
#     t_list = list(str2)
#     s_list.sort()
#     t_list.sort()
    
#     print(s_list)
#     print(t_list)
    
#     if len(s_list) == len(t_list):
#         for i in range(0,len(s_list)):
#             if s_list[i]!= t_list[i]:
#                 return False
#         return True
#     return False        
    
# s = "anagram"
# t = "nagaram"
# if valid_anagram(s,t):
#     print("Valid anagram")
# else:
#     print("invalid anagram")


##METHOD 3 :  LEETCODE METHOD
# BAsically same as above but more neat

# def isAnagram(s: str, t: str):
#     if len(s) == len(t):
#         s = ''.join(sorted(s))
#         t = ''.join(sorted(t))
#         for i in range(0, len(s)):
#             if s[i] !=t[i]:
#                 return False
#         return True
#     return False

# s = "anagram"
# t = "nagaram"
# if isAnagram(s,t):
#     print("Valid anagram")
# else:
#     print("invalid anagram")


# ==============================================================================================


# --->Check if the number is Palindrome or not         ###########

#if reverse of number is same as number then its a palindrome number

## METHOD 1: By converting into string (hack hai)

# num = "22222"
# if num == num[::-1]:
#     print("valid palindrome")
# else:
#     print("invalid palindrome")


## METHOD 2: Actual way to find palindrome number

# def valid_palindrome(num):
#     temp = num
#     rev = 0
#     while (num>0):
#         digit = num%10
#         rev = rev*10 + digit
#         num = num//10
#     if (rev == temp):
#         return True
#     else:
#         return False
# number = 1213
# if valid_palindrome(number):
#     print("Valid Palindrome")
# else:
#     print("invalid palindrome")


## --> FIND all the palindrome numbers in given range         ##########

# def valid_palindrome(num):
#     temp = num
#     rev = 0
#     while (num>0):
#         digit = num%10
#         rev = rev*10 + digit
#         num = num//10
#     if (rev == temp):
#         return True
#     else:
#         return False
        
# def valid_palindrome_range(num1, num2):
#     res = []
#     for i in range(num1,num2):
#         if valid_palindrome(i):
#             res.append(i)
#     return res

# print(valid_palindrome_range(1,100))


#---> Check if the given year is Leap or not          #######

# year = 2024 
# if  ( year % 400 == 0 ): 
#   print ( f "{year} is a leap year .") 
# else : 
#   print(f "{year} is not a leap year.")

##





# -->  Sum of digits num=1234;                 #######

#  ( posible inputs : 1234 ,  1-2-34 , -1-1-1-2 , 0000 , 1$2$ )
# in any case, take the input and return the sum of digits present in it

# def sum_of_number(number):
#     res = ""
#     for i in number:
#         if i.isdigit():
#             res+=i
#     print(res)
#     sum_res = sum(int(digit) for digit in res)
#     print(sum_res)

# num = "123/-4"
# sum_of_number(num)


#--> Remove duplicates from the 2d array      ###################

# nums = [[2,2,2,3,4],[4,5,6,6,3]]
# res = []
# for i in nums:
#     temp = []
#     for j in i:
#         if j not in temp:
#             temp.append(j)
#     res.append(temp)            
# print(res)



#--> Check if the given number is prime or not   #############

# def prime_number(num):
#     if num > 1:
#         for i in range (2, int(num/2)+1):
#             if num%i == 0:
#                 return False
#     return True
# number = 33
# if prime_number(number):
#      print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")


#--> print the sum of all prime numbers in given range   ################

# def prime_number(num):
#     if num > 1:
#         for i in range (2, int(num/2)+1):
#             if num%i == 0:
#                 return False
#     return True


# def sum_prime_number(num1,num2):
#     res = []
#     for i in range(num1,num2+1):
#         if prime_number(i):
#             res.append(i)
#     return sum(res)

# print(sum_prime_number(4,10))


# ==============================================================================================


#--> Check if the given ip is valid or not   ################

# def validate_ip(ip):
#     segements = ip.split('.')
#     if len(segements)!=4:
#         return False
#     for segment in segements:
        
#         if not segment.isdigit():
#             return False
#         if int(segment)<0 or int(segment)>255:
#             return False
#         if segment.startswith('0') and len(segment)>1:
#             return False
#     return True
# ip_adress = "202.112.fje.22"
# if validate_ip(ip_adress):
#     print("Valid ip")
# else:
#     print("Invalid ip")


# ==============================================================================================

# List Comprhension in python      ############################

# what is list comphrehension? 
#--> A way to create a new list with less syntax
#--> list = [expression for the iten in iterable]

# Example - Basic usage of list and for loop
# square = []
# for i in range(1,11):
#     square.append(i*i)
# print(square)

# Same example using list comprehension
#
# square = [i*i for i in range(1,11)]
# print(square)

#--> both gives out the same output just using list comprehension the program becomes more
#    effecient and readable

# Some more examples for list comprehensions:

# cubes = [i*i*i for i in range(1,11) if i%2==0]
# print(cubes)

# print([i*i*i for i in range(1, 11) if i % 2 == 0]) 
#above code works too

#words = ["hello", "world", "python"]
# uppercase_words = [word.upper() for word in words]

# sentence = "This is a sample sentence"
# vowels = [char for char in sentence if char in 'aeiou']


# ==============================================================================================

## --> What is Lamda function in python?                     ########

# Python Lambda Functions are anonymous functions means that the function without a name.
# Basically creating one lines of a function
# lambda arguments : expression

# Noraml  Functin creation
# def add(x,y):
#     return x+y
# print(add(3,4))

# Usage of Lambda function
# add_two = lambda x,y : x+y
# print(add_two(3,4))

#Another usage of lambda function
# print((lambda x,y: x+y)(3,4))

# Lambda functions are mostly used in situations where small function is required for
# a short period of time. They are commonly used for arguments to higher order functions,
# such as map, filter and reduce.
# Higher order functions are those which can take other functions as an input

# Below is the example of usage of lambda with higher order functions

# def my_map(my_func, my_items):
#     result = []
#     for item in my_items:
#         new_item = my_func(item)
#         result.append(new_item)
#     return(result)
    
# nums = [3,4,5,6]
# cubed = my_map(lambda x : x*3, nums)
# print(cubed)



    




##  

##Question on rotate the array

## Question on Patterns



# ==============================================================================================
## QUESTIONS ON DICTIONARIES


# .-->  arrdup=[1,2,3,4,6,4,8,4,4,5,6,6,7,7,7,8,9,9,10]   ##########
# # Hint : Find number of dublicate elements and its no of occurance for each element

# arrdup=[1,2,3,4,6,4,8,4,4,5,6,6,7,7,7,8,9,9,10]
# res = {}
# for i in arrdup:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i] =1
# print(res)



# Given Two lists, Merge them into a dictionary      ##########################
# a = ["a", "b", "c", "d"]
# b = [1,2,3,4]
# output should be : {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# a = ["a", "b", "c", "d"]
# b = [1,2,3,4]
# res = {}

# for i in range(len(a)):
#     res[a[i]] = b[i]
# print(res)





# Print a list of numbers, [1,2,3,4] from disctionary s   ##################3

# s = {
#     "a" :{"one":1},
#     "b" :{"one":2},
#     "c":{"one":3},
#     "d":{"one":4},
# }

# res = []
# for i in s:
#     res.append(s[i]["one"])
# print(res)



# # Print a list of numbers, [1,2,3,4] for disctionary s ##############

# s = {
#     "a" :{"one":1},
#     "b" :{"two":2},
#     "c":{"three":3},
#     "d":{"four":4},
# }


# res = []
# for key in s:
#     for inner_key in s[key]:
#         res.append(s[key][inner_key])
# print(res)

# #NOTE: Make sure to do more practice on Dictionary questions

