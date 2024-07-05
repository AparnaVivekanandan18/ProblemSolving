def factorial(num): 
    # Initialise a var
    fact = 1

    if (num == 0 or num ==1):
        return fact
    else:
        while (num > 1):
            fact = fact * num
            num = num - 1
        return fact

# Execution starts here
print("Enter a valid integer: ")
try:
    inputNum = int(input())
except ValueError as e:
    print("This is not a valid Integer :: ", e )

factorialOfNumber = factorial(inputNum)
print("The Factorial of the given number is:", factorialOfNumber)