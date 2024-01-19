# 1.  Sum of digits num=1234;
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


# # 2. Reverse "vikas"

# s = "vikas"
# res = ""
# for i in s[::-1]:
#     res+=i
# print(res)

 

# 3. Reverse word "vikash" in sentence

# sentence="hai this is vikas  vikash haivikash haithisisisvikash vikash hivikashismyname"
# modified_sentence = sentence.replace("vikash", "hsakiv")
# print(modified_sentence)


# 4.  arrdup=[1,2,3,4,6,4,8,4,4,5,6,6,7,7,7,8,9,9,10]
# # Hint : Find number of dublicate elements and its no of occurance for each element

arrdup=[1,2,3,4,6,4,8,4,4,5,6,6,7,7,7,8,9,9,10]
res = {}
for i in arrdup:
    if i in res:
        res[i]+=1
    else:
        res[i] =1
print(res)