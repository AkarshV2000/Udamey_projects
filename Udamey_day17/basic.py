# class User:
#     pass
# #--> First letter of a class name should always be in capital Letter
# #--> we can use pass keyword we want nothing to be inside a class

# user_1 = User()  #creating an object
# user_1.id = "001"  #creating an attributte froman object
# user_1.name = "akarsh"  #we can make as may attributes we want from an object

# # --> an attribute is basically a vraible that is associated with an object

# print(user_1.name)

# --> but we cannot be creating different attributes for different objects
#     That's why we have constructors, which are initialized while creation of a class

class User:
    def __init__(self,user_id, name): # __init__ is a special function used to initialise attributes
        self.id = user_id # user1.id = "001"
        self.name = name  # user1.name = "akarsh"
        self.followers = 0 #we can also create an attribute even if its not defined under __init__
        self.following = 0
# --> __init__ function is going to be called everytime you create an object from a class
        
# --> self keyword is the way to refer tot he object thats going to be created from the class
#     inside the class blueprint
        
    def follow(self, user): #creating a method
        user.followers +=1
        self.following +=1

user_1 = User("001", "akarsh")
user_2 = User("002","akarsh")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


