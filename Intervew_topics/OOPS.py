
# ==============================================================================================

  ####                  OOPS IN PYTHON                  ########

#--> There are 4 main pillars of OOPS

#    1: Encapsulation
#    2: Abstraction
#    3: Polymorphism
#    4: Inheritance



## WHAT IS ENCAPSULATION, EXPLAIN WITH EXAMPLE?

#--> Since python provides access to all the variables and method globally. By
#    using ENCAPSULATION, we can restrict the variable and method access globally
#    by making it private or protected

#    If we are using single underscore (_name) while creating a variable then it's
#    called protected variable. They are assesible inside as well as outside of the
#    class but to assess them outside of the class they need to be called with the
#    object or that particular class in which they are defined

#    if we are using double underscore (__name) while creating a variable then it's
#    called private variable. Pirvate variables are only assesible from inside the 
#    class. You cannot use them oustside of that particular class in which they 
#    defined

##      Example    

# class Myclass:
#     _a = 10       # Protected variable
#     __b = 20      # Private Variable 

#     def info(self):
#         print (f" print a = {self._a}")
#         print(f" print b = {self.__b}")

# obj = Myclass()
# obj.info()   

# OUTPUT:
# print a = 10
# print b = 20

# print(Myclass._a)    # OUTPUT : 10  # Because Protected class can be accessed 
# #                      outside the class with the help of that class or object


# print(Myclass.__b)   # THIS WLL GIVE ERROR , Because private variable cannot be 
# #                      accessed outside the class



## HOW TO CREATE PRIVATE METHODS USING ENCAPSULATION AND HOW TO ACCESS THEM?


# -->Since we cannot access Private methods directly with objects as we were
#    doing with Private Variables, So we have to create another global method
#    where we internally call that private method , SO everytime we call that 
#    global method outside the class , Private method is automatically called

# class Myclass:
#     def __disp1(self):   # Creating a Private Method
#         print (f" THIS IS DISPLAY 1 ")
#     def disp2(self):     # creating a global method
#         print (f" THIS IS DISPLAY 2 ")
#         self.__disp1()   # internally calling private method from global method
        

# obj = Myclass()
# obj.disp2() # This will call both private as well as global method
# print(obj.__disp1)  # THIS WONT WORK IN CASE OF PRIVATE METHODS



## CAN WE CHANGE THE PRIVATE VARIBLE FROM OUTSIDE OF THE CLASS?

# Yes we can, we have to create another method just to change the value

# class Myclass:
    
#     __empid = 101       # Private Variable
#     def change_id(self, new_eid):  # Method to change the private variable
#         self.__empid = new_eid   # assigning new value to private variable

#     def print_id(self):         # Method to print the private variable
#         print(self.__empid)
        
  

# obj = Myclass()
# obj.change_id(107)
# obj.print_id()


# ==============================================================================================


# WHAT IS ABSTRACTION, EXPLAIN WITH EXAMPLE?

#--> Abstraction is a process of hiding the implementation details form the user 
#    only the highligted set of services provided to the user.

#    There are two methods of achiving abstraction
#    1: Abstract class
#    2: Interface

# What is Abstract class ? Give Example?

#--> Abstract class is that class which contain one or more abstract methods.Some 
#    features of abstract class are: 
#    1: Object of an abstract class cannot be created. They require subclasses to 
#       provide imlementation for the abstract method.
#    2: Python provides abc module to work with abstraction
#    3:  we use @abstractmethod decorator to define abstract method

# --> An abstract method is a method that is declared but contains no implementation or body

# EXAMPLE:

# from abc import ABC, abstractmethod    # We need to iimport class ABC and 
#                                          class abstractmethod from module ABC

# class Animal(ABC):                #creating an abstract class
#     @abstractmethod
#     def eat(self):                # abstract method
#         pass
    
# class Tiger(Animal):              #inheriting abstract class
#     def eat(self):                #overriding the abstract method
#         print("eats flesh")
# class Cow(Animal):                #inheriting abstract class
#     def eat(self):                #overriding the abstract method
#         print("eats grass")

# t = Tiger()                      # creating instace from a subclass
# t.eat()                           

# c = Cow()
# c.eat()


##   WHAT IF WE HAVE MORE THEN ONE ABSTRACT METHOD DEFINED IN ABSTRACT CLASS??


#--> if there are more then one abstract method defined in abstractclass, then
#    we have to call both methods in subclass or the subclass will be treated as an 
#    abstract class too

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def voice(self):
#         pass
    
# class Tiger(Animal):
#     def eat(self):
#         print("eats flesh")
#     def voice(self):
#         print("tiger roar")

# class Cow(Animal):           # this subclass wont be considered
#     def eat(self):
#         print("eats grass")

# t = Tiger()
# t.eat()
# t.voice()

# c = Cow()                #  will throw error
# c.eat()


# Method 2: you can create multiple subclasses for each of the abstractmethod present
#           in abstractclass

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def voice(self):
#         pass
    
# class Cow(Animal):
#     def eat(self):
#         print("eats grass")
        
# class Cow2(Cow):       # here we are creating another subclass that inherit
#                          class Cow and implement abstractmethod Voice
#     def voice(self):
#         print("cow Moo's")

# c = Cow2()
# c.eat()
# c.voice()


## USING ABSTRACT METHOD WITH CONSTRUCTORS

# from abc import ABC, abstractmethod

# class Calc(ABC):
#     def __init__(self,value):
#         self.value = value
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
    
# class Res(Calc):
#     def add(self):
#         print(self.value +10)
#     def sub(self):
#         print(self.value-10)
        

# c = Res(100)
# c.add()
# c.sub()





# What is INTERFACE? Explain with example?

#--> Interface is nothing but abstract class which contains only abstract method
#    but not any normal method. Features of interface are:
#    1: We can't create object of interface
#    2: We use interface/abstraction when action is common but not the implementation
#    3: All child class should inerit abstract method


# ==============================================================================================


## WHAT IS POLYMORPHISM? EXPLAIN WITH EXAMPLES?

#--> Polymprhism means ablility to take different forms, when same object shows
#    different behaviour under different conditions. Polymprphism can be implemented
#    by two ways in python
#    1:  Method overloading
#    2:  Method overriding


## WHAT IS METHOD OVERLOADING? EXPLAIN WITH EXAMPLE?

#--> Whenever class contains more then one method with same name and different 
#    types, parameters is called method overloading

## In the below example same method will result in different outputs dependng on
## what type of input its given
# class Person1:
#     def info(self, name = None):
#         if name is not None:
#             print("hello " + name )
#         else:
#             print("Hello Person")

# obj = Person1()
# obj.info()
# obj.info("Akarsh")




## WHAT IS METHOD OVERRIDING? EXPLAIN WITH EXAMPLE?

#--> whenever we write method name with same signature in parent and child class 
#    called method overriding

#--> in below example person2 class overrides the method from its parent class
#    i.e. Person1 class
# class Person1:
#     def info(self):
#         print("this is Person1")

# class Person2(Person1):
#     def info(self):
#         print("this is Person2")

# obj = Person2()
# obj.info()

## In order to print the output from parent class too, then either you creat another
#  object from parent class or use super() keyword

# class Person1:
#     def info(self):
#         print("this is Person1")

# class Person2(Person1):
#     def info(self):
#         super().info()
#         print("this is Person2")

# obj = Person2()
# obj.info()


# ==============================================================================================


### WHAT IS INHERITANCE IN OOPS, EXPLAIN WITH EXAMPLE?    

#-->In Object-Oriented Programming (OOP), inheritance is a mechanism where a new 
#   class (subclass) is based on an existing class (superclass), inheriting its
#   properties and behaviors. 

# class Person1:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"Name is {self.name}, and age is {self.age}")
# class Person2(Person1):
#     def lang(self):
#         print(f"person speaks english language")

# a = Person1("akarsh", 24)
# a.info
# b = Person2("ayush", 26)
# b.info()
# b.lang()

# WHAT ARE DIFFERENT TYPE OF INERITANCE?

#1: SINGLE INHERITANCE : In single inheritance, a subclass inherits from only one 
#                        superclass. like above example

#2: MULTIPLE INHERITANCE : In multiple inheritance, a subclass inherits from more
#                          than one superclass

# class Parent1:
#     def method1(self):
#         print("Parent1 method")

# class Parent2:
#     def method2(self):
#         print("Parent2 method")

# class Child(Parent1, Parent2):
#     def method3(self):
#         print("Child method")

# obj = Child()
# obj.method1()  # Accessing method from Parent1 class
# obj.method2()  # Accessing method from Parent2 class
# obj.method3()  # Accessing method from Child class


#3: MULTILEVEL INHERITANCE : In multilevel inheritance, a subclass inherits from 
#                            another subclass.

# class Grandparent:
#     def method1(self):
#         print("Grandparent method")

# class Parent(Grandparent):
#     def method2(self):
#         print("Parent method")

# class Child(Parent):
#     def method3(self):
#         print("Child method")

# obj = Child()
# obj.method1()  # Accessing method from Grandparent class
# obj.method2()  # Accessing method from Parent class
# obj.method3()  # Accessing method from Child class


# 4: HIERARCHICAL INHERITANCE : In hierarchical inheritance, multiple subclasses 
#                               inherit from the same superclass.

# class Parent:
#     def method1(self):
#         print("Parent method")

# class Child1(Parent):
#     def method2(self):
#         print("Child1 method")

# class Child2(Parent):
#     def method3(self):
#         print("Child2 method")

# obj1 = Child1()
# obj2 = Child2()
# obj1.method1()  # Accessing method from Parent class
# obj1.method2()  # Accessing method from Child1 class
# obj2.method1()  # Accessing method from Parent class
# obj2.method3()  # Accessing method from Child2 class




# WHAT IS SUPER KEYWOARD IN PYTHON , IMPLEMENT WITH INHERITANCE AND CONSTRUCTORS?


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