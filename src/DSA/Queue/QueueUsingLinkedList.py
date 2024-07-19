# Implementing the Queue Opeartions Using Linked List
# The Reason for choosing linked list is because, Inserting at rear end and deletion at front end
# will take time complexity of O(1) only. If we use Array or List --> 
# then we need to shift the elements to other positions, that will take time complexity of O(n).

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None # This is pointing to rear position
        self.queueLength = 0 #Initialise this count variable & update its value during Enqueue-Deque Operation

    def enqueue(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            self.queueLength = self.queueLength + 1
            print("Item ::", item, " is inserted as first element")
        else:
            temp = self.head
            preValue = temp.value
            self.head = new_node
            new_node.next = temp
            self.queueLength = self.queueLength + 1
            print("Item:: ", item, " is inserted before the element ", preValue)

    def deque(self):
        if self.head is None:
            print("Queue is empty")
        else:
            temp = self.head
            iterate_count = 0 
            #Because this points to header already
            lenn = (self.queueLength - 2)
            while(iterate_count < lenn):
                temp = temp.next
                iterate_count = iterate_count + 1
            
            lastNodeItem = temp.next.value
            temp.next = None
            self.queueLength = self.queueLength - 1
            print("Item :: ", lastNodeItem, "is removed from Queue")

    def displayQueue(self):
        # Display the linked List in Reverse Order
        temp1 = self.head
        iterate_count = 0
        temp_list = []
        while(iterate_count <= self.queueLength):
            if temp1 is None:
                break

            temp_list.append(temp1.value)
            temp1 = temp1.next
            iterate_count =  iterate_count + 1                
            
        
        print("-------- Here the Queue------")
        # Since reverse() returns None, printing it directly would give None
        # Because the reverse happens in-place !!
        temp_list.reverse()
        print(temp_list)

    

#Execution Begins Here
myQueue = Queue()

def execution():
    print("Enter 1 -> To perform EnQueue")
    print("Enter 2 -> To perform DeQueue")
    print("Enter 3 -> To display all the elements")
    print("Enter 4 -> To Terminate the execution")

while True:
    try:
        execution()
        print("Enter your choice")
        inp = int(input())
    except ValueError as e:
        print("Invalid Integer", e)

    match inp:
        case 1:
            print("Enter the element to be inserted")
            item = int(input())
            myQueue.enqueue(item)
            continue
        case 2:
            myQueue.deque()
            continue
        case 3:
            # display in FIFO order
            myQueue.displayQueue()
            continue
        case 4:
            break



