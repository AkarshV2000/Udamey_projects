
## NOTE:   STRING METHODS  ##

# 1: isalnum()--> Returns True if string is alphanumeric
# 2: isalpha()--> Returns True if string contains only alphabets
# 3: isdigit()--> Returns True if sting contains only digit
# 4: isspace()--> Returns True if string contains only whiltespaces
# 5: isupper()--> Returns True if string is in uppercase
# 6: islower()--> Returns True if sting is in lowercase
# SYNTAX:   s.isdigit()

## NOTE :  SEARCHING FOR SUBSTRINGS   ##

# 1: endswith(s1:str)--> Returns True if string ends with substring S1
# 2: satrtswith(s1:str)--> Returns True if string starts with substring S1
# 3: count(substring) --> Returns number occurances of substring in the string
# 4: find(s1) --> Returns lowest index from where S1 starts in the string. If string not found , return -1
# 5: rfind(s1)--> Returns highest index from where S1 starts in the string. If string not found , return -1
# SYNTAX: num = s.count('s1')
## EXAMPLE
# s = "12345abcd/?395jaj 1929 445"
# s = s.endswith("445")
# print(s)     #True

#NOTE : COVERTING STRINGS   ##

# 1: replace(old,new)-->This function returns the new string by replacing the occurance of old string with in the new string.
# 2: lower()--> Returns string by converting every character in lowercase
# 3: upper()--> Returns string by converting every character in uppercase
# 4: capitalize()--> Returnss a copy of this string with only the first character capitalized.
# SYNTAX: s = s.lower()



## NOTE :    .split() and .join() methods in python  ##

#--> .split() :  converts string to a list.
#                The split method breaks up a string at specified separator and
#                returnd a list of strings. By default a sparator is a whotespace
#                syntax: string.split(separator, maxsplit)
#                here both arguments (separator, maxsplit) are optional 


# EXAMPLE:

# s = " I am Akarsh Verma"
#res = s.split()    # By default it takes whitespace as a separator
#print(res)

# s = "202.33.234.1"
# res = s.split('.')  # we have to give seperator as '.'
# print(res)            output : ['202', '33', '234', '1']

# s = "202.33.234.1.4.666.112"
# res = s.split('.', 4)       # using maxsplit as 4
# print(res)            output : ['202', '33', '234', '1', '4.666.112']



#--> .join() :  converts list to a string. The join() method takes all the items
#               in an iterable and join them into a single string
#               Syntax : separator.join(iterable)
#               it has no default value as a seperator, so we have to give it

# EXAMPLES

# s = ["Akarsh" , "Verma"]
# res = ' '.join(s)
# print(res)           Output : Akarsh Verma

# s = ["Java" , "Python" , "C++"]
# res = '-->'.join(s)
# print(res)           Output: Java-->Python-->C++

#--> with dictionary it will join the keys
# s = {"Java": 1 , "Python":2 , "C++":3}
# res = '-->'.join(s)
# print(res)           Output: Java-->Python-->C++







## QUESTIONS ON STRINGS


## --> Count cahracters from a string without using Dictionary

# NOTE: ASCII range of a - z : 97 - 122
# NOTE: ASCII range of A - Z : 65 - 90

# s = "aabbbCCccdd"
# s = s.lower()

# for i in range(97,123):
#     count = 0
#     j = chr(i)      # This will change ASCII value into character
    
#     for char in s:
#         if char == j:
#             count+=1
#     if count>0:
#         print(j , ":" , count)


#  -->  Count and remove vowels from a string   ###

# def count_and_remove_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     res = ""
    
#     for char in string:
#         if char in vowels:
#             count +=1
#         else:
#             res+=char
#     return (res, count)
# s = "UsinG Python Program"
# print(count_and_remove_vowels(s))




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



#--> How do you convert a list of integers to a comma seperated string??

# l = [1,2,3,4,5,6]
# res = []
# for i in l:
#     char = str(i)
#     res.append(char)
# res2 = ','.join(res)
# print(res2)



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




## --> PATTERN QUESTION


## Print the output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 


# def print_star(num):
#     for i in range(1, num+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()

# print_star(6)


##--> Reverse of the above pattern

# def print_star(num):
#     for i in range(1, num+1):
#         for j in range(i, num+1):
#             print("*", end=" ")
#         print()

# print_star(6)

# ==============================================================================================

## -->    Check for armstrong Number

# def armstrong_number(num):
#     temp = num
#     res = 0
#     str_num = str(num)
#     n = len(str_num)
    
#     while num>0:
#         digit = num%10
#         res = res+(digit ** n)
#         num = num //10
    
#     if res == temp:
#         return True
#     else:
#         return False
# number = 153
# if armstrong_number(number):
#     print("Valid")
# else:
#     print("Invalid")

        
        

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


## --> Factorial of a number , using loop as well as using Recurrsion   ####

# def factorial(num):
#     res = 1
#     for i in range(1,num+1):
#         res = res*i
#     return res
# print(factorial(5))


##-->   Using recurrsion                ######

# def factorial(num):
#     if num ==0:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(4))

#---> Check if the given year is Leap or not          #######

# year = 2024 
# if(year%4 == 0 and year%100 !=0) or (year %400 == 0):: 
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





# ==============================================================================================
##  DICTIONARIES   ##

##--> In Python, dictionaries are mutable data structures that allow you to store 
#     key-value pairs. Dictionary can be created using the dict() constructor or 
#     curly braces' {}'. Once you have created a dictionary, you can add, remove, or
#     update elements using the methods dict.update(), dict.pop(), and dict.popitem().

# friends = {"Tom": 1, "Jerry":2 }  #a dictionary
# print(friends)

###   HOW TO MODIFYING A DICTONARY??!? 

#--> Printing value of an item
#print(friends['Tom'])    #output : 1

#--> adding an element to the dictionary
# friends['bob'] = 3
# print(friends)       #output : {'Tom': 1, 'Jerry': 2, 'bob': 3}

#-->updating a particular value of an element
#friends['bob']: 4
#print(friends)       #output : {'Tom': 1, 'Jerry': 2, 'bob': 4}

#--> deleteing an element from an dictionary
# del friends['bob']
#print(friends)       #output : {'Tom': 1, 'Jerry': 2}


##  DIFFERENT METHODS IN A DICTIONARY



#--> len():  returns length of a dictionary in int 

# friends = {"Tom": 1, "Jerry":2 }  
#print(len(friends))     #ouptput : 2

#--> keys(): returns keys of a dictionary as a tuple
#friends = {"Tom": 1, "Jerry":2 } 
#print(friends.keys())     #output : dict_keys(['Tom', 'Jerry'])

#--> values(): returns keys of a dictionary as a tuple
#friends = {"Tom": 1, "Jerry":2 } 
#print(friends.values())     #output : dict_values([1, 2])

#--> get(key) : Return value of a key , if key is not found then it None, Instead
#               of throwing ExceptionError
#friends = {"Tom": 1, "Jerry":2 } 
#print(friends.get('Tom'))     #ouptout: 1

#--> pop(key): Remove the item from the dictionary , if key is not found then
#              KeyError will be thrown 
#friends = {"Tom": 1, "Jerry":2 } 
#friends.pop('Tom')
#print(friends)         #output : {'jerry': 2  }



## LOOPING THROUGH A DICTIONARY ##

## Print a list of number [1,2,3,4]

# s = {
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4
# }
# res = []
# for i in s:
#     res.append(s[i])
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

## Method 2:

# a = [1,2,3,4]
# b = ["a","b", "c", "d"]
# res = dict(zip(a,b))
# print(res)







# #NOTE: Make sure to do more practice on Dictionary questions



# ==============================================================================================

##WHAT IS *args and  **kargs n PYTHON ?!? EXPLAIN WITH EXAMPLE

#--> *args(Non-Keyword arguments) allows us to pass variabe number of arguments to the function
#     def sum(a,b):
#     print("sum is", a+b)
#     This program accepts only two numbers, what if you eant to pass more than
#     two arguments, this is where *args comes into play
#    
#     NOTE: name of *args is for just convention, it can be anything   

# EXAMPLe

# def sum(*args):
#     s = 0
#     for i in args:
#         s+=i
#     print("sum is", s)

#sum(10,20)    # here we can give any number of parameters, sum(1,2,3,4,5,5)


#**kargs --> we use ** to take inputs in form of key value pair

#def my_func(**kargs):
#   for i,j in kargs.items():
#       print(i,j)

#my_func(name = "Tom", sport = "Football" , age = 20)


#==============================================================================================


#WHAT IS EXCEPTION HANDELING IN PYTHON? GIVE EXAMPLE

#--> Error in Python can be of two types i.e. Syntax errors and Exceptions. 
#    Errors are problems in a program due to which the program will stop the execution.
#    On the other hand, exceptions are raised when some internal events occur which
#    change the normal flow of the program. 

# Exception Handeling Keywords:
#--> try
#--> except
#--> else
#--> finally

#--> since in python the programm gets terminated as soon as it comes across an 
#     error, in order to avoid that we use exception handeling

# Example 
#print("program ha started")
#print(10/0)  #this will throw ZeroDivisionError
#print("Program has ended")

# Output
# Program has started
# Error

#--> So the first line got executed but as soon as the progamm hits th second line
#    it throws an error and rest of the program never got executed, Below is how 
#    we handle exceptions like this

#print("program has started")
#try:
#   print(10/0)  #this will throw ZeroDivisionError
#except ZeroDivisionError:  # we sepcify the exact error the try block will throw
#    print("Error, Divinding by Zero")
#prnt("Program has ended")

# Output
# Program has started
# Error, Divinding by Zero
#Program has ended

#--> here the program is executed till the end. Execpt block will only get executed
#    only if the statement under try block throws an error, If statement uder try
#    block is fine, then it will skip the except block

#--> We can have multiple except block for one try block, programm will check all
#    the except blocks and whichever matches with the error it will print the content
#    of that particular block, and if it dosent matches with any, then program 
#    will be terminated

# EXAMPLE

#print("program ha started")
#try:
#   print(10/0)  # ZeroDivisionError
#except TypeError:  
#    print("Error, not the int type")
#except ZeroDivisionError:
#   print("Error, Cant bedivided by Zero")  
#prnt("Program has ended")


#--> Statements under else block will run only when  try block throws no exception,
#    so it wont go into except blocks instead it will go into else block, and if the
#    error is present in try-except block, then the else block won't be executed.

#print("program ha started")
#try:
#   print(10/5)  # No error will be thrown
#except TypeError:  
#    print("Error, not the int type")
#except ValueError:
#   print("Error, wrong value ")  
#else:
#   print("entered into else block..") 
#prnt("Program has ended")

#OUTPUT: 
#program ha started
#2.0
#entered into else block..
#Program has ended


#--> Statement under finally block will always be executed no matter if the try
#    statement is throwing an error or not

# EXAMPLE:

#print("program has started")
#try:
#   print(10/5)  # No error will be thrown
#except TypeError:  
#    print("Error, not the int type")
#except ValueError:
#   print("Error, wrong value ")  
#else:
#   print("entered into else block..") 
#prnt("Program has ended")
#finally:
#   print("entered into finally block...")


#OUTPUT: 
#program ha started
#2.0
#entered into else block..
#Program has ended
#entered into finally block...


## HOW DO YOU RAISE AN EXCEPTION ?? GIVE EXAMPLE 

#--> To raise your exception from your own methods you need to use raise keywor
#    e.g. :  raise ExceptionClass("Your argument")

# EXAMPLE:

# def enterage(age):
#     if age <= 0:
#         raise ValueError("Only positive intergers are allowed")
    
#     if age %2 ==0:
#         print("age is even")
#     else:
#         print("age is odd")

# num = 0 
# enterage(num)






# s = '''Day ** Sun#Mon#Tue

# Month*Jan#Feb

# Num*1##2#3

# Alpha***a#b##c'''



# res = {}

# a
# # s = s.split("*")
# # print(s)

# keys = []

# for i in s:
#     inner = ""
#     if i == "*":
#         break
#     else:
#         inner+=i



 

# # [{Day: [Sun, Mon, Tue]},

# # {Month: [Jan, Feb],

# # { Num: [1, 2, 3],

# # {Alpha: [a, b, c]

# # ]



# Write a program to find out the longest ascending order sub list in a given list.

 

# Exmaple:

 

# I/P: 3, 4, 2, 3, 4, 5, 6, 1, 3, 5, 3, 6

 

# O/P: 2, 3, 4, 5, 6

# def longset_sublist(num):
#     res = []
#     k = 
#     # for i in range(2, len(nums)+1):
#     #     temp = []
#     #     if num[i] > num[i-1]:
#     #         count+=1
#     #         temp.append(num[i])
#     i , j = 0 , 1
    
#     while j <= len(nums):
#         temp = []
#         if nums[j] > nums[j-1]:
#             temp.append[i]
#             j+=1
#             i+=1
#         else:
#             i = j
#             j+=1
