from linked_list import LinkedList

def check_if_circular(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return False  # Empty or single-node linked list

    slow_ptr = linked_list.head
    fast_ptr = linked_list.head.next

    while fast_ptr and fast_ptr.next:
        if slow_ptr == fast_ptr:
            return True  # Loop detected
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return False  # No loop

ll = LinkedList([1, 2, 3, 4, 5])
# ll.head.next.next.next.next = ll.head
if check_if_circular(ll):
    print("Circular LL")
else:
    print("Not circular")