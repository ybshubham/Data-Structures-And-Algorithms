from doubly_linked_list import DoublyLinkedList, Node


def find_largest_node(dll):
    current = max_node = dll.head

    while current:
        if current.data > max_node.data:
            max_node = current
        current = current.next
    return max_node

dll = DoublyLinkedList([1,2,3,5])
largest_node = find_largest_node(dll)
if largest_node:
    print(f"Largest node: {largest_node.data}")
else:
    print("Linked list is empty")