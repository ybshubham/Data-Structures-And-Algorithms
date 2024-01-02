from doubly_linked_list import DoublyLinkedList

def check_palindrome(dll):
    if not dll.head:
        return False

    start = dll.head
    end = dll.get_tail()

    while start and end and start != end:
        if start.data != end.data:
            return False
        start = start.next
        end = end.prev   
    return True

dll = DoublyLinkedList(['l', 'e', 'v', 'e', 'l'])
if check_palindrome(dll):
    print("Given DLL is palindrome")
else:
    print("Not palindrome")