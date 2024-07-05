def factorial(num):
    if (num== 0 or num == 1):
        return 1
    else:
        return num * factorial(num-1)

# Execution Starts Here
print("Enter the Input number::")

try:
    inputNum = int(input())
except ValueError as e:
    print("This is not a valid integer")

factNum = factorial(inputNum)
print("The Factorial is ::", factNum)
