from doubly_linked_list import DoublyLinkedList

'''
Approach 1 : While traversing, check current node with next node and remove
Complexities:
    Time : (n)
    Space: O(1)
'''
def remove_duplicates(dll):
    if not dll.head:
        return
    
    current = dll.head

    while current and current.next:
        if current.data == current.next.data:
            next_node = current.next.next
            current.next = next_node
            if next_node:
                next_node.prev = current
        else:
            current = current.next

dll = DoublyLinkedList([4,4,4,4,6,8,8,10,12,12])
remove_duplicates(dll)
dll.forward_traversal()