'''
Note : 
For question : sort biotonic doubly linked list
Ans : use any normal sorting technique (bubble sort, insertion sort, selection sort, ..)

A biotonic DLL is a DLL which is either :
    - first increasing and then decreasing
    - strictly increasing
    - strictly decreasing
'''

from doubly_linked_list  import DoublyLinkedList

def bubble_sort(dll):
    dll_len = dll.get_length()

    for i in range(dll_len):
        current = dll.head
        for j in range(0, dll_len - i - 1):
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
            current = current.next

def insertion_sort(dll):
    dll_len = dll.get_length()

    for i in range(1, dll_len):
        key_node = dll.get_node_at_index(i)
        key_data = key_node.data

        current = key_node.prev
        while current.prev and key_data < current.data:
            current.next.data = current.data
            current = current.prev
        
        current.next.data = current.data
        current.data = key_data

def selection_sort(dll):
    if not dll.head:
        return

    current = dll.head

    while current:
        min_node = current
        runner = current.next

        while runner:
            if runner.data < min_node.data:
                min_node = runner
            runner = runner.next

        # Swap data between current and min_node
        current.data, min_node.data = min_node.data, current.data

        current = current.next


dll = DoublyLinkedList([2, 5, 7, 12, 10, 6, 4, 1])
# dll = DoublyLinkedList([1,3,4,5,8,9,10])
# dll = DoublyLinkedList([10,8,7,5,2,1])
bubble_sort(dll)
# insertion_sort(dll)
# selection_sort(dll)
# dll.forward_traversal()
