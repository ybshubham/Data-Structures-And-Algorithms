class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, arr=None):
        self.head = None

        if arr:
            self.create_from_list(arr)
    
    def create_from_list(self, arr):
        for item in arr:
            if self.head is None:
                self.insert_at_beginning(item) 
            else:
                self.insert_at_end(item)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    print("Position out of bounds")
                    return
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_from_end(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

    def delete_from_position(self, position):
        if position == 0:
            self.delete_from_beginning()
        else:
            current = self.head
            for _ in range(position):
                if current is None:
                    print("Position out of bounds")
                    return
                current = current.next
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

    def forward_traversal(self):
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")

    def reverse_traversal(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <--> ")
            current = current.prev
        print("None")

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                print(f"{key} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"{key} not found in the list")
    
    def get_node_at_index(self, index):
        if not self.head:
            return None

        current = self.head
        while current and index:
            current = current.next
            index -= 1

        return current

    def update_node_value(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next
        print(f"{old_value} not found in the list")

    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def get_tail(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next
        return current

# Example usage:
# dll = DoublyLinkedList([1,2,3,4,5])
# dll.forward_traversal()
# dll.reverse_traversal()
