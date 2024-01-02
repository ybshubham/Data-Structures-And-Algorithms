from doubly_linked_list import DoublyLinkedList, Node

def find_pair(dll, sum):
    if dll.head is None:
        return None

    pairs = []
    head = dll.head
    tail = dll.get_tail()

    while head and tail and head != tail:
        if head.data + tail.data == sum:
            pairs.append([head.data, tail.data])
            head = head.next
            tail = tail.prev
        elif head.data + tail.data > sum:
            tail = tail.prev
        else:
            head = head.next
    
    return pairs

dll = DoublyLinkedList([1,2,4,5,6,8,9])
sum = 99
pairs = find_pair(dll, sum)
if pairs:
    print(f"pairs: {pairs}")
else:
    print("No pair with given sum")