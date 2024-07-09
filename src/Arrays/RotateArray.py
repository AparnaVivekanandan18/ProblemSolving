# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# I am here .....Using List as an array in Python

def rotate(num_list, steps):
    total_len_list = len(num_list)
    temp = total_len_list - steps

    rotate_list = num_list[temp:total_len_list]
    initial_list = num_list[:temp+1]
    rotate_list.extend(initial_list)
    return rotate_list

# Execution Starts Here
try:
    print("enter the steps to be rotated right")
    steps = int(input())
    print("Enter the no.of.input numbers")
    len_num = int(input())

    num_list = []
    print("Enter the input numbers")
    for i in range(len_num):
        num = int(input())
        num_list.append(num)
except ValueError as e:
    print("Invalid Input !")

rotated_array_list = rotate(num_list, steps)
print("The Rotated List", rotated_array_list)
