         ###########             FILE HANDELING                ##############

##different modes in file handeling:

# r: open for reading(default mode)
# w: open for writing, truncating the file first(basically overrite the file)
# x: create a new file and open it for writing
# a: open for writing, appending to the end of the file if it exists
# b: open binary files
# t: text mode(default)
# +: open a disk file for updating(read an write the file) eg: r+, w+, a+


### how to open a file and read its content.
# f = open("example_file.txt","r")
# data = f.read()
# print(data)
# f.close()


### how to write in a file

# f = open("example_file.txt", "")
# f.write("I need to work")
# f.close()

# NOTE: "w" which imeas write mode, basically w overrites the whole file,
#       which means the the whole cotent of file will be deleted and then the given
#       content will be added to it , where as "a" which is append will add the
#       string after whatever is already present in file

# NOTE: "w", "a", if file doesd not exisits then these modes will create a new file

## how to append in a file

# f = open("example_file.txt", "a")
# f.write("\nHi I am Akarsh")
# f.close()

# IMPORTANT
# r+ = read and overrite, pointer is at start (no truncate)
# w+ = read + overwrite, pointer is at end (truncate)
# a+ = read and append, pointer is at end (no truncate)

# Text in file: "Hey I am Akarsh"

# f = open("example_file.txt", "r+") 
# # in read mode(r) the pointer is at the very beginning, so if we want to change
# # things up from the beginning then we use r+ mode     
# f.write("abc")  #output: abc I am Akarsh (changed first 3 characters with abc)
# # and now the pointer is at spacebar
# print(f.read()) #output: I am Akarsh
# f.close()


# Text in file: "Hey I am Akarsh"

# f = open("example_file.txt", "w+")
# #in write mode the whole files get truncated, so nothing will be printed
# print(f.read())  # output: Nothing
# f.write("abc")
# print(f.read())  #still no output since the pointer is at end but the file will have "abc"
# f.close()

# # Text in file: "Hey I am Akarsh"
# f = open("example_file.txt", "a+")
# print(f.read())
# # in this case the output will be blank space since append puts the pointer at the 
# # very end but the file will still have "Hey I am Akarsh"
# f.write("abc")
# print(f.read())
# # in this case the output will be blank space again,file will have "Hey I am Akarshabc"
# f.close


##          With Syntax in file handeling   #### 

# with syntax basically does the same thing as opeing a file but in more professional 
# way, and you dont have to give f.close(), sine with closes it automatically

# with open("example_file.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("example_file.txt", "w") as f:
#     f.write("not Akarsh anymore")



####        deleting a file  ###########

# we can delete file by using os module

# import os
# os.remove("example_file.txt")

## Example: From a file containing numbers seperated by comma, prin the count of even numbers
# 1,2,45,55,86,76

def count_even_numbers():
    with open("example_file.txt", "r") as f:
        count = 0
        data = f.read()
        new_data = data.split(",")
        for i in new_data:
            if int(i) %2 == 0:
                count+=1
    return count

print(count_even_numbers())




