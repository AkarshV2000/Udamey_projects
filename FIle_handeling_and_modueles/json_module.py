import json
# JSON file is stored mostly with .json format and there are no comments in the json file

#loads() method is used to parse any jason data
# data = '{"var1": "Akarsh", "var2":"Verma"}'  #some json data
# parsed  = json.loads(data)
# print(parsed)

#dumps() method is used to make your json data into java compatible form
# data = {
#     "first_name": "Akarsh",
#     "second_name": "Verma",
#     "Age": 25,
#     "DOB": "26/02/1999",
#     "Married" : False            #in js 'False' is written as 'false
# }

# jsdata = json.dumps(data)
# print(jsdata)

#load() method is used to extract json data from a particular json file
# with open("data.json", 'r') as file:
#     parsed = json.load(file)
#     for i in parsed:
#         print(i)


## How to create a json file from python

# def write_json(data, filename = "json_data2.json"):
#     with open(filename,'w') as f:
#         json.dump(data,f, indent = 4)

# data = [1,4,6,8,]
# write_json(data)


## How to update json file which is aleady present

def write_json(data, filename = "data.json"):
    with open(filename, "w") as f:
        json.dump(data,f , indent = 4)

with open("data.json") as json_files:
    data = json.load(json_files)
    temp = data["names"]
    y = {"first_name": "Akarsh", "age": 24}
    temp.append(y)

write_json(data)