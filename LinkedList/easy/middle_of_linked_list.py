'''
# print the middle of linked list
'''
from LinkedList.linked_list import LinkedList

def find_middle(linked_list):
    if not linked_list.head:
        return None

    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr

ll = LinkedList([1, 2, 3, 4, 5])
middle = find_middle(ll)
if middle:
    print(f"middle of linked list is: {middle.data}")
else:
    print("Linked List is empty, can't find middle")
