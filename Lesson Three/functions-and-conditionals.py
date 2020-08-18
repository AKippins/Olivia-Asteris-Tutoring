# Write a function which will sum a range of integers starting from one going up and including a 
# value entered by the user. Write a main function which takes the number entered by the user 
# and calls the function, outputting the result to the user. 

# Our example number is 10

# Calculating the sum of an number 
user_input = range(10)
total = 0

for number in user_input:
	total = number + total
	print(total)




def NumberTotal(number):
    user_input = range(number)
    total = 0
    
    for number in user_input:
	    total = number + total
	    print(total)

number = int(input("Put in a number.\n"))
def NumberTotal(number):
   print(sum(range(1, number)))

NumberTotal(number)

# Built in functions in Python
print()
range()


# This is the same as what's abobe but a different way of doing it. 
print(sum(range(10)))

def HelloWorld(name):
    print("Hello " + name + "! Welcome to our world!!!!")

print()
HelloWorld("Pineapple")
HelloWorld("Apple")
HelloWorld(1)


# Booleans are True/False
# Integers are numbers
# Lists
# Strings are sentences
# Float, Doubles, Long are decimals. 

if __name__ == "__main__":
    number = input("Gimme a number and i'll give you the sum from 1 to that number.\n")
    NumberTotal(number)