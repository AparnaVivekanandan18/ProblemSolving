

var1 = 'ireland'
print(var1[6])
print(var1[-1])

print("".join(reversed(var1)))


# Updating a String
var2 = "Hello Hello"
# Python strings are immutable, hence we cannot update the chracters directly.
# Method 1:

list1 = list(var2)
list1[4] = 'p'

print("Before", list1)
var2 = "".join(list1)
print("Updated String", var2)
