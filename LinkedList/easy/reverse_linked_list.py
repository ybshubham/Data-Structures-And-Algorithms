from linked_list import LinkedList

def reverse(ll):
    prev = None
    current = ll.head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    ll.head = prev

ll = LinkedList([1,2,3,4,5])
ll.traverse()
reverse(ll)
ll.traverse()