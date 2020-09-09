# Write a function which computes the solutions of any quadratic equation of the form ax2 + bx + c = 0. 
# Write a main function which takes the three coefficients from the user and calls the function, 
# outputting the results to the user. Make sure that your function will not try to evaluate any square roots of negative numbers.

# When we get a problem
# Break the problem down
# Take note of anything thats important
# We get more managable pieces
# Get it into terms we can understand
# Find a solution
# Scale up

# X^2 + 12X + 32
# X = -8 & X = -4
import math 
def quadratic_solver(a, b, c):
    if b*b - (4*a*c) >= 0:
        solution_1 = (-b + math.sqrt(b*b - (4*a*c)))/2*a
        solution_2 = (-b - math.sqrt(b*b - (4*a*c)))/2*a
        print(solution_1, solution_2)
    else:
        print("You're trying to evaluate the square root of a negative number or zero, Try agin")




if __name__ == "__main__":
    a = int(input('Enter an a value'))
    b = int(input('Enter an b value'))
    c = int(input('Enter an c value'))
    quadratic_solver(a, b, c)