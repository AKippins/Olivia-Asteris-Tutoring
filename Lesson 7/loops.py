array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("For loop with list")
for number in array:
    print(number)
    if number == 5:
        break

print("For loop with range()")
# Range(1, 10) makes [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in range(1, 10):
    print(number)


# Queue
# Just a line. First In First Out
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Stacks 
# Stack of plates, or a stack of cards. First In Last Out
# Push and Pop
# Push 1 into our Array
# [] <- 1
# [1]
# Push 2 into our Array
# [1] <- 2
# [1, 2]
# Pop from our array
# [1] -> 2
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("While loop with list")
while array:
    number = array.pop()
    print(number)

print(array)
print(len(array))