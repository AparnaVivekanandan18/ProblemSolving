
def push(item,myStack,top,max_memory_size):
    if top >= max_memory_size: # Check Stack Overflow
        print("Stack OverFlow!")
    else:
        myStack.insert(top,item)
        print("The item is inserted into stack", item, "\n")

def displayStack(myStack):
    for itemIndex in range(len(myStack)):
        print("Actual Stack Order", myStack[itemIndex])

def pop(myStack,top):
    if len(myStack) <= 0:
        print("Stack UnderFlow")
    else:
        item = myStack[top]
        myStack.remove(item)
        print("The item is popped out", item, "\n")

#Execution begins here
# Initialise a stack using List
# Here i am not going to use the list operations, rather I am going to convert Stack's logic into code

myStack = [] #Initialising Stack using list - Empty Stack
top = 0 #Global Variable
memory_size = 100

def execution():
    print("Enter 1 -> To push an item into Stack")
    print("Enter 2 -> To pop an item from Stack")
    print("Enter 3 -> To display elements in Stack")
    print("Enter 4 -> To check if the Stack is_empty")
    print("Enter 5 -> To terminate the execution")
    inp = int(input())
    return inp

while True:
    try:
        inp = execution()  
    except ValueError as e:        
        print("Invalid Integer !")

    match inp:
        case 1:
            print("Enter an element to be inserted")
            item = input()
            push(item,myStack,top,memory_size)
            continue
        case 2:
            pop(myStack,top)
            continue
        case 3:
            displayStack(myStack)
            continue
        case 4:
            continue
        case 5:
            break
    