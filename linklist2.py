class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None
        
        return self.head

# fuction to remove duplicate node
    def deleteDuplicates(self):
        curr = self.head
        if not curr:
            return self.head
        prev = curr
        curr = curr.next
        while(curr):
            if prev.data == curr.data:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return self.head
        
            
        
        
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data,"--->",end=" "),
            printval = printval.next
        print("None")
        

        

llist = SLinkedList()
llist.Atbegining(1)
llist.Atbegining(2)
llist.Atbegining(3)
llist.Atbegining(4)
llist.Atbegining(4)
print("original Linkedlist:")
llist.LListprint()
print("Removed element from Linklist:")
llist.RemoveNode(2)
llist.LListprint()
llist.deleteDuplicates()
print("Removed duplicate element from Linklist:")
llist.LListprint()

