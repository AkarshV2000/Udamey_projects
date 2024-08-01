##########   OOP   ###########
# -->  In opject oriented programming we are trying to model real life objects and those 
#      object have things(attributes) and also can do things(methods)
# -->  The things that they have are their attributes and these are usually modeled with
#      variables and the things that they can do
# -->  And the things that they can do are called methods and they are modled by functions
# -->  So essentially, an object is just a way of combining some piece of data and some
#      functionality altogether in the same thing.
#
# --> In OOP a class is a blueprint, And we call these individual objects generated form 
#      these blueprints an object

#--> class name is always starts with a capital Letter

# import turtle 
# timmy = turtle.Turtle() #creating an object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("black", "blue")
# timmy.forward(100)

# my_screen = turtle.Screen()
# # object.atribute
# print(my_screen.canvheight)
# #my_sreen is the objectwe created and canvasheight is the attribute assosiatedwith that object
# my_screen.exitonclick()

# import prettytable 
# #find the packages on pyepi.org , after finding the desired package run pip install (package name)

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)



###########   Coffee Machine Project with OOP   #############

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker= CoffeeMaker()
menu = Menu()




is_on = True
while is_on:
  options = menu.get_items()
  choice= input(f" what you'd like to take: {options}: ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
        
    
    
  







