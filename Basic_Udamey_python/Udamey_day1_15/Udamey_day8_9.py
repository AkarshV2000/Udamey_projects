#    **DICTIONARY**


# student_grades ={"Akarsh":100,"Ayush":90, "Himanshu":80,"Harshit":70, "Ansh":60,"Deepak":99}
# res = {}
# for grade in student_grades:
#     if (student_grades[grade]) >= 90 and (student_grades[grade]) <=100 :
#         res[grade] = "Outstanding"
#     if (student_grades[grade]) >= 80 and (student_grades[grade]) < 90:
#         res[grade] = "Outperformed"
#     if (student_grades[grade]) >= 70 and (student_grades[grade]) < 80:
#         res[grade] = "Need Improvement"
#     if (student_grades[grade]) < 70:
#         res[grade] = "Fail"
# print(res)
        
# Nesting a List in a Dictionary

# travel_log = {"UK":{"Cities_Visited":["dehradoon", "Mussorie", "Nainital", "Hridwar"," Rishikesh"], "totoal_Visit":10}}
# print(travel_log["UK"]["Cities_Visited"])

# country = input()
# visit = int(input())
# cities = eval(input())
# travel_log = [
#     {
#     "country":"France",
#     "visit": 4,
#     "cities":["a","b","c"]
#     },
#     {
#     "country":"Australia",
#     "visit": 2,
#     "cities":["d","e","f"]
#     }
#     ]
# def add_new_country(name,total_visit,cities_name):
#     new_country = {}
#     new_country["country"] = name
#     new_country["visit"] = total_visit
#     new_country["cities"] = cities_name
#     travel_log.append(new_country)

# add_new_country(country, visit, cities)
# print(f"{travel_log[2]['country']} is my fav")
# print(travel_log)

import os
bids ={}
bidding_finished = False
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with the highest bid of {highest_bid}")
while not bidding_finished:
    name = input("please enter your name: ")
    bid= int(input("please enter your tatal bid: $"))
    bids [name] = bid
    bid_continue = input("are there any other bidders? type 'Yes' or 'No': ")
    if bid_continue == "No":
        bidding_finished = True
        highest_bidder(bids)
    else:
        os.system('cls')
