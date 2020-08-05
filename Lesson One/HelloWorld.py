# This is what's called a comment. 
# Python likes to get the job done.
# I wanna do things quicker than a Java
# Float (00000000 00000000 00000000 00000000) vs Double. (00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000)

# Bits 0 or 1
# Byte is a collection of bits. Is 8 bits long. (00000000) these are the same (0), (00000000 00000000 00000000 00000000)
# Binary is base 2 unique numbers. 0 & 1
# Decimal is base 10 unique numbers. 0 - 9
# Hexidecimal is base 16 unique numbers. 0 - 9 A, B, C, D, E, F (0-F)


# Olivia is 16
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0, 1, 10, 11, 100 ... 1111

# This is a string.
Name = "Hello Olivia!!!"
# This is an integer
Age = 16
# This is a float
MonthsTillBirthday = .90011300
# This is a double
MonthsTillBirthdayDouble = .9001130012012030
# This is a list
TodoList = ["Take A Nap", "Eat Dinner", "Play Animal Crossing", "Ignore School"]
# This is a boolean
Over18 = False


Name = "Hello Olivia!!!"

if Age > 15:
    print(Name)
else:
    print("Who are you?")

print("Your Todo's today are as following")

for item in TodoList:
    print(item)