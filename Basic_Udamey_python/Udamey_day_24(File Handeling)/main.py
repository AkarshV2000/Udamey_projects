
## Either you use this method to open a file 

# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

## Or you can use below method (much preferred)

## default mode is read
# with open("my_file.txt") as  file:
#     content = file.read()
#     print(content)

# ## In order to write to a file we need to change the mode too

# with open("my_file.txt" , mode='w') as  file:
#     file.write("\n New text")

# ## NOTE : if a file name dosent exist in write mode("w"), then it will create a new file and
# ##        and write the contents to it.

# with open("my_file.txt_pt2" , mode='w') as  file:
#     file.write("\n New text")



#### Write an automation script to use the names provided in Names directory. And use those Names 
#    to write letter for each person using the format provided in starting letter directory
#    And add those letter in ready to send directory

with open("/home/akarsh/Udamey_projects/Basic_Udamey_python/Udamey_day_24(File Handeling)/Names/input_names.txt", mode="r") as names:
    name = names.readlines()  # this will give you a list of each line
new_name = []
for i in name:
    x = i.strip()     # this is an useful method to strip of blank spaces in front and back of a string
    new_name.append(x)

   

with open("/home/akarsh/Udamey_projects/Basic_Udamey_python/Udamey_day_24(File Handeling)/starting_letter/starting_letter.txt" , "r+") as letter:
    content = letter.read()


for i in new_name:

    with open(f"/home/akarsh/Udamey_projects/Basic_Udamey_python/Udamey_day_24(File Handeling)/Ready_to_send/letter_for_{i}.docx", mode = "w") as letter:
        new_content = content.replace("[Name]", i)
        letter.write(new_content)
