import sys

# Write a function which computes the slope and y-intercept for the line passing 
# through the points (x1, y1) and (x2, y2). Use this formula for the slope: (y2 - y1) / (x2 - x1)  
# and this one for the y-intercept: b = y1 – m*x1. Write a main function which takes the values 
# of x1, y1, x2 and y2 from the user and calls the function, outputting the results to the user.

# Write a function for me that will take 2 numbers and add them together. 
def add(x, y):
    return x + y

# Write a function for me that will take 2 numbers and subtract them. 
def subtract(x, y):
    return x - y

# # Write a function for me that will take 2 numbers and multiply them together. 
# def multiply(x, y):
#     return x * y


def multiply(x, y):
    try:
        return x * y
    except TypeError as error:
        print("Something went wrong. We ended up with two incompatible data types. Found the following error: ", error)
        # sys.exit(-1)

# # Write a function for me that will take 2 numbers and divide them. 
# def divide(x, y):
#     return x / y

# Write a function for me that will take 2 numbers and divide them. 
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as error:
        print("An error has occurred, please try again. Found the following error: ", error)
        # sys.exit(-1)
    

# addition = add(6,4)
# subtraction = subtract(3,1)
# multiplication = multiply(2, 3)
# division = divide(4,2)

# print(addition, subtraction, multiplication, division)

def slope_finder(x1, x2, y1, y2): 
    y_difference = subtract(y2, y1) 
    x_difference = subtract(x2, x1)
    return divide(y_difference, x_difference)

def y_intercept_finder(y1, x1, slope): 
    slope_times_x1 = multiply(slope, x1)
    return subtract(y1, slope_times_x1)

def user_prompt():
    x1 = int(input("What's the x1?"))
    y1 = int(input("What's the y1?"))
    x2 = int(input("What's the x2?"))
    y2 = int(input("What's the y2?"))
    # Defining the slope
    slope = slope_finder(x1, x2, y1, y2)
    # Defining the Y intercept
    y_intercept = y_intercept_finder(y1, x1, slope)
    print("This is the slope: " + str(slope)  + "This is the y intercept: " + str(y_intercept)) 


# Write a main function that we can work with. 
if __name__ == "__main__":
    user_prompt()
    



