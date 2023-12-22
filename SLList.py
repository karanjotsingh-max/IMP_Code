# creating a node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# creating a singly linked list class
class SLL:
    def __init__(self):
        self.head=None

    def insertatBeg(self,data):
        # creating object
        new_node=Node(data) 
        if(self.head is None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    
    def insertatEnd(self,data):
        new_node=Node(data)
        temp_node=self.head
        while(temp_node):
            if(temp_node.next is None):
                break      
            temp_node=temp_node.next
        if(self.head is None):
            self.head=new_node
        else:
            temp_node.next=new_node
    
    #Deletion
    def deleteatBeg(self):
        if(self.head is None):
            return
        self.head=self.head.next

    def deleteatEnd(self):
        if(self.head is None):
            return
        current_node=self.head
        while(current_node.next!=None):
            prev_node=current_node
            current_node=current_node.next
        prev_node.next=None
    
    def deleteatInd(self,index):
        pos=0
        if(index==pos and self.head!=None):
            self.head=self.head.next
        else:
            current_node=self.head
            while(current_node.next!=None and pos!=index):
                pos+=1
                prev_node=current_node
                current_node=current_node.next
            prev_node.next=current_node.next

    #Updation of nodes
    def updateatInd(self,data,index):
        pos=0
        if(index==pos and self.head!=None):
            self.head.data=data
        else:
            current_node=self.head
            while(current_node.next!=None and pos!=index):
                pos+=1
                current_node=current_node.next
            current_node.data=data
        
    #SLL Traversal/Printing
    def printSLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data,"-> ",end="")
            current_node=current_node.next
        print("None")

    def middllist(self):
        pos=0
        tpose=0
        if(self.head is None):
            return
        else:
            current_node=self.head
            while(current_node.next!=None):
                pos+=1
                current_node=current_node.next
            current_node=self.head
            while(current_node.next!=None and tpose!=(pos+1)//2):
                tpose+=1
                current_node=current_node.next
            return current_node.data






# create a new linked list
sllist1=SLL()
#adding values to LL
a=int(input("Enter Range:"))
for i in range(a):
    sllist1.insertatEnd(int(input("Enter Value:")))
    # sllist1.insertatBeg(int(input("Enter value:")))

# sllist1.deleteatInd(3)
    
# sllist1.updateatInd(3,2)

print("Middle of SLL:",sllist1.middllist())

#printing sll
print("Singly Linked List:",end="")
sllist1.printSLL()            