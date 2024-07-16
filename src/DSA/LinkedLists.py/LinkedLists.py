
# Structuring a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        pass

# Structuring a Linked List
class LinkedList:
    def __init__(self):
        self.head = None #Initialising head as None, whenever the class gets instantiated.

    # Insert at Beginning
    def insertAtBeginning(self, data):
        #Instantiating a new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node # Make head pointer to point the newly created node, as its going to be header henceforth
            return
        
    
    # Insert at nth position
    def insertAtMiddle(self,data,index):
        #Instantiating a new node1

        new_node = Node(data)
        #Initialise a variable
        position = 0
        if index == position: # Insert at beginning
            self.insertAtBeginning(data)
        
        # Inserting after the mentioned position
        # 0 is considered as inserting at beginning

        curr_node = self.head
        position = position + 1
        while(curr_node != None):
            if position == index:
                new_node.next = curr_node.next
                curr_node.next = new_node
            curr_node = curr_node.next
            position = position + 1
        return

    # Insert at End position
    def insertAtEnd(self,data):
        new_node = Node(data)
        curr_node = self.head
        while (curr_node.next != None):
            curr_node = curr_node.next
        
        if curr_node.next is None:
            curr_node.next = new_node
        return
    
    # Delete node at specified position in a linked list
    def deleteNode(self,index):
        
    # Display Linked List
    def displayLinkedList(self):
        curr_node = self.head
        print("---------- Linked List ----------------")
        while(curr_node):
            print(curr_node.data)
            curr_node = curr_node.next
        print("---------- Linked List ----------------")
        return


def execution() -> int:
    print("Choose the options\n\n")
    print("Enter 1 -->  Inserting a node at beginning")
    print("Enter 2 -->  Inserting a node after nth position")
    print("Enter 3 -->  Inserting a node at last position")
    print("Enter 4 -->  Deleting a node after nth position")
    print("Enter 5 -->  Updating the node at nth position")
    print("Enter 6 -->  Display the linked list")
    print("Enter 7 -->  Search the position of an element")
    print("Enter 8 -->  Exit")
    print("\n\n")
    inp = int(input())
    return inp
    

# --------------------Execution Starts Here---------------------------------------------
# Creating a new Instance of class LinkedList - Globally
# This Instance is maintained in run-time memory --> until run-time execution terminates !
linkedList = LinkedList() 

while True:
    try:
        inp = execution()  
    except ValueError as e:        
        print("Invalid Integer !")

    match inp:
        case 1:
            print("Enter the data to be inserted at beginning")
            data = int(input())
            linkedList.insertAtBeginning(data)
            continue # To continue the execution
        case 2:
            print("Enter the data to be inserted")
            data = int(input())
            print("Enter the position, after which the data to be inserted")
            index = int(input())
            linkedList.insertAtMiddle(data,index)
            continue # To continue the execution
        case 3:
            print("Enter the data to be inserted")
            data = int(input())
            linkedList.insertAtEnd(data)
            continue # To continue the execution
        case 4:
            print("Enter the position, after which the date to be deleted")
            data = int(input())
            linkedlist.
        case 5:
            print("")
        case 6:
            linkedList.displayLinkedList()
            continue # To continue the execution
        case 7:
            print("")
        case 8:
            print("------------------Terminating the run-time execution---------------------------")
            break

