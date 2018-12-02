class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def detect_loop(self):
        a_node = self.head
        b_node = self.head
        while a_node and b_node and b_node.next:
            a_node = a_node.next
            b_node = b_node.next.next
            if a_node==b_node:
                print("LOOP FOUND")
                return
llist = LinkedList()
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
  
# Create a loop for testing 
llist.head.next.next.next.next = llist.head 
llist.detect_loop()