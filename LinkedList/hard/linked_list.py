class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, arr=None):
        self.head = None

        if arr:
            self.create_from_list(arr)

    '''Create linked list from list/array'''
    def create_from_list(self, arr):
        self.head = Node(arr[0])
        prev_node = self.head

        for item in arr[1:]:
            node = Node(item)
            prev_node.next = node
            prev_node = node

    ''' Basic Operations'''
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def remove_from_beginning(self):
        if not self.head:
            print("Linked list is empty. Nothing to remove.")
            return

        self.head = self.head.next

    def remove_from_last(self):
        if not self.head:
            print("Linked list is empty. Nothing to remove.")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    '''Insertion, modification & Deletion at specific positions'''
    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current:
                break
            current = current.next

        if not current:
            print("Index out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node

    def update_at_index(self, index, data):
        current = self.head
        for _ in range(index):
            if not current:
                print("Index out of bounds. Cannot update.")
                return
            current = current.next

        current.data = data

    def remove_from_index(self, index):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.remove_from_beginning()
            return

        current = self.head
        for _ in range(index - 1):
            if not current or not current.next:
                print("Index out of bounds. Cannot remove.")
                return
            current = current.next

        current.next = current.next.next

    '''Traverse & Search'''
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    '''Miscellaneous'''
    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def is_empty(self):
        return self.head is None

    '''Advanced Operations'''
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge(self, other_linked_list):
        if not other_linked_list.head:
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = other_linked_list.head

    def insert_after_node(self, node, data):
        if not node:
            print("Node cannot be None.")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def insert_before_node(self, node, data):
        if not node or not self.head:
            print("Node or linked list is empty. Cannot insert.")
            return

        if node == self.head:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        while current.next and current.next != node:
            current = current.next

        if not current.next:
            print("Node not found. Cannot insert.")
            return

        new_node.next = current.next
        current.next = new_node

    def remove_by_value(self, data):
        if not self.head:
            print("Linked list is empty. Cannot remove.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            print("Data not found. Cannot remove.")
            return

        current.next = current.next.next

    def remove_after_node(self, node):
        if not node or not node.next:
            print("Node or next node is None. Cannot remove.")
            return

        node.next = node.next.next

    def remove_before_node(self, node):
        if not self.head or not node or node == self.head:
            print("Linked list is empty or node is None. Cannot remove.")
            return

        if self.head.next == node:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.next != node:
            current = current.next

        if not current.next:
            print("Node not found. Cannot remove.")
            return

        current.next = current.next.next

    def delete_linked_list(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
        self.head = None

# Example usage:
# linked_list = LinkedList([1, 2, 3, 4, 5])
# linked_list.traverse()
# index = linked_list.search(4)
# is_empty = linked_list.is_empty()
# linked_list.reverse()
# linked_list.delete_linked_list()
