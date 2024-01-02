from linked_list import LinkedList

def find_cycle_start(head):
    if not head and not head.next:
        return None
    
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        # found collision point
        if slow_ptr == fast_ptr:
            break
    
    # no cycle detected
    if not fast_ptr or not fast_ptr.next:
        return None

    fast_ptr = head
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    
    return slow_ptr

# Example Usage:
ll = LinkedList([1,2,3,4,5])
ll.head.next.next.next.next.next = ll.head.next

# Find the start of the cycle
start_of_cycle = find_cycle_start(ll.head)
print(start_of_cycle.data)
