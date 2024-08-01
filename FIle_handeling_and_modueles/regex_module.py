        #######          REGEX MODULE             ########
#--> regular expressions aew a way to search special patterns in a raw text
import re

# # search() method, return the indices of the patter and return None if not found
# data1 = "python is an object based language"
# pattern1= "python"
# match = re.search(pattern1, data1, re.IGNORECASE)
# print(match.group())
# print(match)
# re.IGNORECASE is used to search for case insensitive data known as one of the flags
# we can use match.group() function to print the value in indices
# NOTE: match is also an inbuilt method. so match is match.group() is different from
#       the match we used as a variable

# data2= "abababdjfjfbababa"
# pattern2 = "ab"

# match = re.findall(pattern2, data2, re.IGNORECASE)
# print(match)
# re.findall() returns a list of all the occurances


###    Character class in REGEX

# --> In Python, regex character classes are sets of characters or ranges of 
# characters enclosed by square brackets [].

# For example, [a-z] it means match any lowercase letter from a to z. 
#Some examples of character class



# [abc]	:    Match the letter a or b or c
# [abc][pq]: Match letter a or b or c followed by either p or q.
# [^abc]:	 Match any letter except a, b, or c (negation)
# [0-9]	:    Match any digit from 0 to 9. inclusive (range)
# [a-z]:     Match any lowercase letters from a to z. inclusive (range)
# [A-Z]	:    Match any UPPERCASE letters from A to Z. inclusive (range)
# [a-zA-z]:  Match any lowercase or UPPERCASE letter. inclusive (range)
# [m-p2-8]:  Ranges: matches a letter between m and p and digits from 2 to 8, but not p2
# [a-zA-Z0-9_]:	Match any alphanumeric character


# pattern3 =r'[aeiou]'
# data3 = "akarsh is a human"

# matches = re.findall(pattern3, data3, re.IGNORECASE)
# print(matches)

# pattern4 = r'[^a-z0-9 ]'
# data4 = "Akarsh is a Human ## from @Earth "
# matches = re.findall(pattern4, data4, re.IGNORECASE)
# print(matches)

# # NOTE: In the context of Python, the r before the string indicates that the
# #        string is a raw string. This means that escape sequences 
# #       (like \n, \t, etc.) are not processed. Instead, the backslashes 
# #        are treated as literal characters.



#####            SPECIAL SEQUENCES IN REGEX           ###########

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D" {including spaces}

# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"

# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"

# \b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain", r"ain\B"

# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
# NOTE: r'.'--> this will maych evertything present in the string, including spaces and special characters
# EXAMPLE

# def find_matches(pattern= str, data = str):
#     matches = re.findall(pattern , data)
#     return matches

# data = "Akarsh is 24 years old && his DOB is 2000 %"

# print(find_matches("\d", data)) #output : ['2', '4', '2', '0', '0', '0']
# print(find_matches("\w", data)) #it will include everything except spaces and special characters
# print(find_matches("\AAkarsh", data))
# print(find_matches("%\Z", data))
# print(find_matches(".", data))
# pattern = r'\bold\b'
# res = re.finditer(pattern, data)
# for match in res:
#     print(match.start(), "-->" , match.group(), end = " ")


# QUES: Extract all the dates present in example_fie.txt

# def extract_dates():
#     with open("example_file.txt", 'r') as f:
#         data = f.read()
#         pattern = r'\d{2}-\d{2}-\d{4}'
#         match = re.findall(pattern, data)
#     return match

# print(extract_dates())


#######                METAcharacters in REGEX        #######

# . (DOT)	Matches any character except a newline.
# ^ (Caret)	Matches pattern only at the start of the string.
# $ (Dollar)	Matches pattern at the end of the string
# * (asterisk)	Matches 0 or more repetitions of the regex.
# + (Plus)	Match 1 or more repetitions of the regex.
# ? (Question mark)	Match 0 or 1 repetition of the regex.
# [] (Square brackets)	Used to indicate a set of characters. Matches any single character in brackets. For example, [abc] will match either a, or, b, or c character
# | (Pipe)	used to specify multiple patterns. For example, P1|P2, where P1 and P2 are two different regexes.
# \ (backslash)	Use to escape special characters or signals a special sequence. For example, If you are searching for one of the special characters you can use a \ to escape them
# [^...]	Matches any single character not in brackets.
# (...)	Matches whatever regular expression is inside the parentheses. For example, (abc) will match to substring 'abc'


# data = "Aaakkkaarrshhh anddddd ayayaya ayush areaareareeee brothersssss"
# pattern1 = r'a+' # this wil give output if  'a' occurs one or more time

# print(re.findall(pattern1, data, re.IGNORECASE))
# #OUTPUT: ['Aaa', 'aa', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'aa', 'a']

# pattern2 = r'aa+'
# print(re.findall(pattern2, data, re.IGNORECASE))
# #OUTPUT: ['Aaa', 'aa', 'aa']

# pattern3 = r'(aa)+'
# print(re.findall(pattern3, data, re.IGNORECASE))
# #OUTPUT: ['Aa', 'aa', 'aa']

# pattern4 = r'a*'   #NOTE: '*' matches 0 or more that 0 characters while '+' matches 1 or more than 1 character
# print(re.findall(pattern4, data, re.IGNORECASE))

# EXAMPLE: Find out the email addresss in given data

# DATA = "email address of Akarsh is vermaakarsh2000@gmail.com and ayush's is vayush303@gmail.com"
# pattern = r'\w+@\w+\.\w+'
# print(re.findall(pattern, DATA))


#EXAMPLE: Feth themobile numbers
data = "mobile number is 132-5667-354 and 6392646079"
pattern = r'\d{3}-?\d{4}-?\d{3}'
print(re.findall(pattern, data))