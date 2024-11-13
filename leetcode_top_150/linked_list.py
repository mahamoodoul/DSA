class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def insert_at_middle(self, data, position):
        
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return 

        current = self.head
        current_position = 0
        while current and current_position < position -1:
            current = current.next
            current_position += 1
        if not current:
            print("position out of bound")
            return
        new_node.next = current.next
        current.next = new_node


    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def update(self, old, new):
        current = self.head
        while current:
            if current.data == old:
                current.data = new
                return
            current = current.next
        print("not found")

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if not current:
            print("not found")
            return
        
        previous.next = current.next
        current = None
    
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")


#test code

ll = LinkedList()
ll.insert_at_last(10)
ll.insert_at_last(20)
ll.insert_at_last(30)
ll.insert_at_last(40)
ll.insert_at_first(5)
ll.insert_at_first(1)
ll.traverse()
ll.insert_at_middle(70,4)
ll.traverse()
# Search for a node
position = ll.search(30)
print("Position of 30:", position)  # Expected: Position of 30: 5
ll.update(30, 31)
ll.traverse()
ll.delete(20)
ll.traverse()