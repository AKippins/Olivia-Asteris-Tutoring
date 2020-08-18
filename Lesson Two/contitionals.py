# Different cases when writing
# Kebab Case: writing-words-with-a-stick-through-them (Liv likes Kebabs)
# Snake Case: writing_words_that_slither_on_the_ground
# Camel Case: writingWithNewWordsCapitalized

# Python 2 vs 3
# Important for today is print statements.
# This: print("This is correct")
# This is wrong: print "This is gonna break and make life difficult"

# Range
# range(x, y)
# You'll start at x and end BEFORE y 

# Positions
# 0|1|2|3|4|5|6|7
# | | | | | | | |
# |0|1|2|3|4|5|6|



# for turtle in range(1, 6):
#     print ("turtle")

# Local Variables and Scope
# turtle is a local variable

# for turtle in range(1, 6):
#     print (turtle)

# france = 7

# print("Addition")
# for turtle in range(1, 6):
#     print (turtle + france)

# print("Subtract")
# for turtle in range(1, 6):
#     print (turtle - france)

# print("Multiply")
# for turtle in range(1, 6):
#     print (turtle * france)

# print("Divide")
# for turtle in range(1, 6):
#     print (turtle / france)

# print("Modulo")

# france = 2

# 
# for turtle in range(0, 6):
#     if (turtle % france == 1):
#         print ("odd")
#     elif (turtle == 0):
#         print ("zero")
#     else: 
#         print ("even")

# ASCII is how computers write letters. 
# This is ASCII 
# :-) XD :^(

# Truth Tables
#    And Table
# I'm trying to make a sandwich
# Top Row is Peanut Butter
# Left Column is Jelly
# Can I make a Peanut Butter and Jelly?
# 
#      |  T  |  F
# -----|-----|-----
#   T  |  T  |  F
# -----|-----|-----
#   F  |  F  |  F
# 
# I need to shop for clothes
# I need to eat lunch

#    Or Table
# Top Row Shopping
# Left Column Lunch with friends. 
# Do I need to talk to somebody?
#      |  T  |  F
# -----|-----|-----
#   T  |  T  |  T
# -----|-----|-----
#   F  |  T  |  F
# 

blue = True
red = True

# if (blue):
#     print("I have the color Blue")
#     if (red):
#         print("I have the color Red")
#         print("I can make purple")

# print(" ")

if (red or blue):
    print("I can still draw")

if (red):
    print("I have the color Red")
if (blue):
    print("I have the color Blue")
if (blue and red):
    print("I can make purple")
else:
    print("Awwww Shucks!!!!")