# Write a function which decides if any year entered from the keyboard is a leap year. 
# Write a main function which takes the year from the user and calls the function, 
# outputting the results to the user.

# When we get a problem
# Break the problem down. 
# We get more managable pieces
# Get it into terms we can understand
# Find a solution
# Scale up

# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
# but these centurial years are leap years if they are exactly divisible by 400. For example, 
# the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.

# TODO: Ask the user for the year. Doneish. 
# TODO: Year mod 100 to see if it's a centurial year. If so, then we mod 400 to see if it is a leap year. Done.
# TODO: Using modulo by 4 if equal to 0 then it is a leap year. Done
# TODO: Print to the user. Done
# TODO: Make our main function. Done

def leap_year_finder(year): 
    year = int(year)
    if year % 100 == 0 and year % 400 == 0:
        print("It's a leap year")
    elif year % 100 == 0 and not year % 400 == 0: 
        print("It's not a leap year")
    elif year % 4 == 0: 
        print("It's a leap year")
    else:
        print("It's not a leap year")


if __name__ == "__main__":
    year = int(input('Enter a year'))
    # year = "2000"
    leap_year_finder(year)




