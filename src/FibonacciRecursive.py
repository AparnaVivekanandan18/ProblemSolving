
def fibo(i):
    if  (i ==0 or i ==1):
        return i
    else:
        return fibo(i-1) + fibo(i-2)
    
# Execution Starts Here
try:
    print("Enter the range of fibonnaci numbers to be generated:")
    inputvar = int(input());
except ValueError as e:
    print("Invalid Integer ::", e)

fibonacciSeries1 = ""
for i in range(inputvar):
    fibonacciSeries = fibo(i)
    fibonacciSeries1 = fibonacciSeries1 + " " + str(fibonacciSeries)

print("fibonacci series ::", fibonacciSeries1)

