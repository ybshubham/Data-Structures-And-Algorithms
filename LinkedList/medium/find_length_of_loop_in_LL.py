from linked_list import LinkedList

def count_nodes(head):
    if not head:
        return 0
    count = 1
    temp = head.next
    while temp != head:
        count += 1
        temp = temp.next
    return count

# Example Usage:
ll = LinkedList([1,2,3,4,5])
ll.head.next.next.next.next.next = ll.head

# Find the start of the cycle
total_nodes = count_nodes(ll.head)
print(total_nodes)


'''
Note:
    -   If in given linked list it is not necessary that last node would point to first to make circular LL
        It could be any node pointing to any node to make circular LL, then:
            1. first find the point of collision
            2. from collision point, start a iterating till you visit same node
            3. You'll get total node count
'''