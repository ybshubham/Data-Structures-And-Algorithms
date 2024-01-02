from doubly_linked_list import DoublyLinkedList

def insert_in_sorted_order(dll, key):
    if not dll.head:
        dll.insert_at_beginning(key)
        return

    current = dll.head
    index = 0

    while current and current.data < key:
        current = current.next
        index += 1
    dll.insert_at_position(key, index)

dll = DoublyLinkedList([2,5,8,10,12])

insert_in_sorted_order(dll, 11)
dll.forward_traversal()