# Structuring a Node to be inserted
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    # Initialise a variable here
    def __init__(self):
        self.top = None

    def push(self,item,myStack):
        new_node = Node(item)
        if self.top != None:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node

    def pop(self):
        if self.top == None:
            print("Stack Underflow")
        else:
            item = self.top.value
            temp = self.top.next
            self.top.next = None
            self.top = temp
            print(item, "---------------- The Item popped out ------------------")
        
    def displayStack(self):
        print("Displaying Stack Items in LIFO order")
        temp = self.top
        while(temp!= None):
            print(temp.value)
            temp= temp.next

#Execution Begins Here
myStack = Stack()

def execution() -> int:
    print("Enter 1 -> To Push an Item")
    print("Enter 2 -> To pop an Item")
    print("Enter 3 -> To display item")
    print("Enter 4 -> To terminate the execution")
    inp = int(input())
    return inp

while True:
    try:
        print("Enter your choice")
        inp = execution()
    except ValueError as e:
        print("Invalid Integer ::", e)

    match inp:
        case 1:
            print("Enter the item to be inserted")
            item = int(input())
            myStack.push(item,myStack)
            continue
        case 2:
            myStack.pop()
            continue
        case 3:
            myStack.displayStack()
            continue
        case 4:
            break
