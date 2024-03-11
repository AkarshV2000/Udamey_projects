# -->  Sum of digits num=1234;  #######

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




# -->  Inheritance in oops             ###########

# class Person1:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"Name is {self.name}, and age is {self.age}")
# class Person2(Person1):
#     def lang():
#         print(f"person speaks english language")

# a = Person1("akarsh", 24)
# a.info
# b = Person2("ayush", 26)
# b.info()
# b.lang()



# --> super() keyword in python         ##############
#     The super() function is used to give access to methods and properties of a 
#     parent or sibling class. The super() function returns an object that represents
#     the parent class.  

# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def info(self):
#         print(f"Name is {self.name}, id is {self.id}")

# class Programmer(Employee):
#     def __init__(self, name, id , lang):
#         super().__init__(name,id)  # this will inherit the name and id from superclass
#         self.lang = lang
#     def info(self):
#         print(f"name is {self.name}, id is {self.id}, language is {self.lang}")

# employee = Employee("Akarsh", "432")
# employee.info()

# programmer = Programmer("Ayush", "4959" , "Python")
# programmer.info()





#--> Method Overriding in python   ###############
#   Method overriding is a concept in object-oriented programming (OOP) 
#   where a subclass provides a specific implementation of a method that is
#   already defined in its superclass. This allows the subclass to modify or
#   extend the behavior of the method inherited from the superclass.

# class Shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius,radius)

#     def area(self):
#         return 3.14 * super().area()
    
# c = Circle(5)
# print(c.area())