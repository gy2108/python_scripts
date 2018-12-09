#Implementing Stack using LinkedList
class Stack_Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.root=None

    def isEmpty(self):
        if self.root==None:
            return True
        return False
    def push(self,data):
        node = Stack_Node(data)
        node.next=self.root
        self.root=node
    def pop(self):
        if self.isEmpty():
            return "Stack empty!!!"
        temp = self.root
        self.root=self.root.next
        return temp.data
    def peek(self):
        if self.isEmpty():
            return "Stack empty!!!"
        return self.root.data
    
stack = Stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
print("{} is popped".format(stack.pop()))
print("Top element is {}".format(stack.peek()))
