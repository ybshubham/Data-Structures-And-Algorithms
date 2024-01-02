from linked_list import LinkedList

'''
Approach 1 : Traverse linked list & delete next node if duplicate
Complexities:
    Time Complexity: O(n)
    Space Complexity: O(1)
'''
def remove_duplicates(linked_list):
    if not linked_list.head:
        print("Please provide a valid linked list")
        return None

    current = linked_list.head

    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next # here we are not moving current, we are just updating valye of "current.next" 
        else:
            current = current.next
        

'''
Approach 2 : Create pointer for first occurance of every element.
Complexities:
    Time Complexity: O(n)
    Space Complexity: O(1)
'''
def remove_duplicates(head):
    if not head:
        print("Please provide a valid linked list")
        return None

    first_occurrence = head
    current = head.next

    while current:
        if current.data != first_occurrence.data:
            first_occurrence.next = current
            first_occurrence = current

        current = current.next

    first_occurrence.next = None

ll = LinkedList([11, 11, 11, 21, 43, 43, 60, 60, 60])
remove_duplicates(ll)
ll.traverse()

