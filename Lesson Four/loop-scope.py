dummy_list = [1, 2, 3, 4, 5, 6, 7, 8]
outside_loop = 0
print("Outside loop starts at: " + str(outside_loop) + "\n")

for number in dummy_list:
    inside_loop = 0
    print("Inside loop starts at: " + str(inside_loop) + "\n")
    inside_loop += number
    print("Inside loop is currently: " + str(inside_loop) + "\n")
    outside_loop += number
    print("Outside loop is currently: " + str(outside_loop) + "\n")

print("Final total of the inside loop is: " + str(inside_loop) + "\n")
print("Final total of the outside loop is: " + str(outside_loop) + "\n")