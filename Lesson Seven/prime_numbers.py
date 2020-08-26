# Write a function which determines if a number is prime or composite. 
# Write a main function which takes the number from the user and calls 
# the function, outputting the results to the user.

# When we get a problem
# Break the problem down
# Take note of anything thats important
# We get more managable pieces
# Get it into terms we can understand
# Find a solution
# Scale up

# Prime only has the factors one and itself. Composites are anything else. 2 is a prime number, but anything that is divisible 
# by 2 it's not a prime number. 

# KISS: Keep It Simple Stupid
# DOTS: Don't Over Think Shit


# Example is 5
# Only factors if 5 is prime are 1 & 5
# 5 is prime because nothing between 1 & 5 is divisible by 5
# Loops can break
# Loops stop when the end condition is met
# For loops end condition is the end of the list
# While loops end condition is when the conitional comes out to be False.

def prime_number_finder(number):
    number = int(number)
    if number == 1:  
        print("It's not prime")
    for divisor in range(2, number):
        if number % divisor == 0:
            print ("It's not a prime number")
            break
        else:
            print("It's a prime number")
            

prime_number_finder(47055833459)