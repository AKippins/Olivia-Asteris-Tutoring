# Write a function which will sum a range of integers starting from one going up and including a 
# value entered by the user. Write a main function which takes the number entered by the user 
# and calls the function, outputting the result to the user. 

# I'm defining the function 'NumberTotal' as whatever number you put in. 
# Then im taking the range of 1 to the number and saving it as 'WorkingRange'
# and then adding all the numbers in 'WorkingRange' and saving it as 'WorkingSum', then printing it. 
def NumberTotal(number):
    WorkingRange = range(1, number)
    WorkingSum = sum(WorkingRange)
    print(WorkingSum)

if __name__ == "__main__":
    number = input("Gimme a number and i'll give you the sum from 1 to that number.\n")
    NumberTotal(number)note