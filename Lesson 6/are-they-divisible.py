# Write a function which decides, given the numbers a and b, if the larger is a 
# multiple of the smaller. Write a main function which takes the two numbers 
# from the user and calls the function, outputting the results to the user. 

def multiple(a, b):
    larger_one = max(a, b)
    smaller_one = min(a, b)
    if larger_one % smaller_one == 0: 
        print("its a multiple")
    else: 
        print("its not a multiple")

if __name__ == "__main__":
    a = int(input("Enter your first number")) 
    b = int(input("Enter your second number"))
    multiple(a,b)



# When we get a problem
# Break the problem down. 
# We get more managable pieces
# Get it into terms we can understand
# Find a solution
# Scale up

# Figure out what's bigger and what's smaller. 
# We're working with whole numbers. No decimals. No remainders.
# We've figured out we need to use modulo because it'll tell us if we have a remainder or not. 
# 4 / 2 = 2
# 5 / 2 = 2.5
# 5 / 2 = 2 r 1
# 6 / 3 = 2
# 7 / 2 = 3 r 1
# n / 2 = 