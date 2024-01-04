from doubly_linked_list import DoublyLinkedList

'''
Approach : Using HashSet
Complexities:
    - Time : O(n)
    - Space : O(n)
'''
def remove_duplicates(dll):
    if not dll.head:
        return

    hashset = set()

    current = dll.head

    while current:
        if current.data not in hashset:
            hashset.add(current.data)
        else:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

        current = current.next

dll = DoublyLinkedList([8,4,4,6,4,8,4,10,12,12])
remove_duplicates(dll)
dll.forward_traversal()