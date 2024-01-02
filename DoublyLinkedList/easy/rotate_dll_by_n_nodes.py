from doubly_linked_list import DoublyLinkedList


def rotate_clockwise(dll, rotate_by_nodes):
    dll_length = dll.get_length()
    if (not dll.head) or (rotate_by_nodes % dll_length == 0):
        return
    
    effective_rotation = rotate_by_nodes % dll_length

    start = dll.head
    for _ in range(dll_length - effective_rotation):
        start = start.next
    
    # making prev node of start as last node
    start.prev.next = None

    end = start
    while end.next:
        end = end.next
    
    end.next = dll.head
    dll.head.prev = end

    start.prev = None
    dll.head = start


def rotate_counter_clockwise(dll, rotate_by_nodes):
    dll_length = dll.get_length()

    if (not dll.head) or (rotate_by_nodes <= 0) or (rotate_by_nodes % dll_length == 0):
        return

    rotate_by_nodes = rotate_by_nodes % dll_length

    current = dll.head
    count = 1

    while count < rotate_by_nodes and current:
        current = current.next
        count += 1

    if not current:
        return

    new_head = current.next
    new_head.prev = None
    current.next = None

    last_node = new_head
    while last_node.next:
        last_node = last_node.next

    last_node.next = dll.head
    dll.head.prev = last_node

    dll.head = new_head


# dll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
dll = DoublyLinkedList([])
rotate_counter_clockwise(dll, 5)
# rotate_clockwise(dll, 1)
dll.forward_traversal()