class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList():
    def __init__(self, value):
        self.value = value
        self.head = None
    

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node


    def insert(self, value, index):
        i = 0
        new_node = Node(value)
        node = self.head
        prev_node = None
        
        if index == 0:
            new_node.next_node = node
            self.head = new_node
            return
        
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
          
        prev_node.next_node = new_node
        new_node.next_node = node


    def remove(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        
        self.size -= 1
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        if index == len(self.items) - 1:
            current.next = None
        else:
            current.next = current.next.next


    def printL(self):
        node = self.head
        while node:
            if node.next_node:
                print(node.value, end=' -> ')
            else:
                print(node.value)
            node = node.next_node
        print()
    
#==============================================
linked_list = LinkedList(16)

linked_list.add_node(5)
linked_list.add_node(11)
linked_list.add_node(36)
linked_list.add_node(57)
linked_list.add_node(73)

linked_list.printL()

linked_list.remove(2)

linked_list.printL()