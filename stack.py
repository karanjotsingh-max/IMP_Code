# Stack using SinglyLinkedList

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    
    def isempty(self):
        if(self.head is None):
            return True
        else:
            return False
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def peek(self):
        cnode=self.head
        return cnode.data
    
    def pop(self):
        self.head=self.head.next
    



Stack1=SLL()
#Pushing in an element
for i in range(int(input("Enter Size of Stack:"))):
    Stack1.push(int(input()))

print("Top:",Stack1.peek())

#Popping out an element
Stack1.pop()

print("After Popping, Top:",Stack1.peek())
    


    




