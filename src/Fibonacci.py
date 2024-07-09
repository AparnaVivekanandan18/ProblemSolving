
# Class with __init__ function
class Fibo:
    def __init__ (self, rangeInp): # initialise a class variable here
        self.rangeInpp = rangeInp
    
    def generateFibo(self):
        # Initialise
        n1 = 0
        n2 = 1
        fibonacci = str(n1) + " " + str(n2)
        for i in range (2, self.rangeInpp):
            n3 = n1 + n2
            fibonacci = fibonacci + " " + str(n3)
            n1 = n2
            n2 = n3
        return fibonacci



#Execution starts here...
print("Enter the range of fibonnaci numbers to be generated:")

try:
    rangeInput = int(input())
except ValueError as e:
    print("Invalid Integer !")

fiboObj = Fibo(rangeInput)
fiboseries = fiboObj.generateFibo()

print("fibonacci Series ::", fiboseries)