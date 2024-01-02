from doubly_linked_list import DoublyLinkedList

def remove_all_occurances(dll, key):
    if not dll.head:
        return

    current = dll.head

    while current:
        if current.data == key:
            if current.prev:
                current.prev.next = current.next
            else:
                dll.head = current.next

            if current.next:
                current.next.prev = current.prev
        current = current.next
        
dll = DoublyLinkedList([2,2,10,8,4,2,5,2])
key = 2
remove_all_occurances(dll, key)
dll.forward_traversal()