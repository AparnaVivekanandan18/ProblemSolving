# Remove duplicates in an array and return the length of an array
# Note: We can use "Set()" built-in function to return the elements without duplicate
# Note: We can also use Collection "OrderedDict.fromKey() method to remove the duplicates, while retaining the order"

import array as arr

def remove_duplicates(inp_array):
    inp_array_len = len(inp_array)
    new_array = arr.array('i', [])
    for i in range(inp_array_len):
        if inp_array[i] not in new_array:
            new_array.append(inp_array[i])
    return new_array

#Execution starts here
try:
    print("Enter length of an array")
    arr_len = int(input())
    print("Enter array elements")
    new_array = arr.array('i',[]) #Initialise an arry
    for i in range(arr_len):
        arr_ele = int(input())
        new_array.insert(i, arr_ele)
except ValueError as e:
    print("Not a valid Integer")

print("The array is :: \n", new_array)
new_array = remove_duplicates(new_array)
print("The duplicates removed", new_array)