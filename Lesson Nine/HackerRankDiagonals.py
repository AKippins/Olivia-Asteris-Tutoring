"""
[1,2,3] Left Position [0][0] Right Positon [0][2]
[4,5,6] Left Position [1][1] Right Positon [1][1]
[7,8,9] Left Position [2][2] Right Positon [2][0]

[1,2,3,4] Left Position [0][0] Right Positon [0][3]
[4,5,6,7] Left Position [1][1] Right Positon [1][2]
[7,8,9,0] Left Position [2][2] Right Positon [2][1]
[4,3,2,1] Left Position [3][3] Right Positon [3][0]

[1,2,3,4,5] Left Position [0][0] Right Positon [0][4]
[4,5,6,7,6] Left Position [1][1] Right Positon [1][3]
[7,8,9,0,9] Left Position [2][2] Right Positon [2][2]
[4,3,2,1,0] Left Position [3][3] Right Positon [3][1]
[6,7,8,9,0] Left Position [4][4] Right Positon [4][0]



    0      1      2
[[1,2,3][4,5,6][7,8,9]]

len = 3
index1 = 0 = gonna go up by 1
index2 = len - 1 = gonna go down by 1

for numbers in table:
numbers = [1,2,3] Left Number [left_position] Right Number [right_position]
numbers = [4,5,6]
numbers = [7,8,9]


"""

def diagonalDifference(arr):
    # Write your code here
    arr = list(arr)
    left_diagonal = 0
    right_diagonal = 0
    left_position = 0
    right_position = int(len(arr)) - 1
    
    for numbers in arr:
        left_diagonal += numbers[left_position]
        right_diagonal += numbers[right_position]

        left_position = left_position + 1
        right_position = right_position - 1 
        
    


    bigger_one = max(left_diagonal, right_diagonal)
    smaller_one = min(left_diagonal, right_diagonal)
    
    difference = bigger_one - smaller_one
    difference = abs(difference)
    return(difference)