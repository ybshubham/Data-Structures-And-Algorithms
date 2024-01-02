from linked_list import LinkedList

'''
Approach 1 : Traverse linked list & delete next node if duplicate
Complexities:
    Time Complexity: O(n)
    Space Complexity: O(1)
'''
def get_intersection(linked_list_1, linked_list_2):
    new_ll = LinkedList()

    if not linked_list_1.head or not linked_list_2.head:
        print("Please provide valid linked lists to find intersection")
        return new_ll

    current1 = linked_list_1.head
    current2 = linked_list_2.head

    while current1 and current2:
        if current1.data == current2.data:
            new_ll.insert_at_end(current1.data)
            current1 = current1.next
            current2 = current2.next
        elif current1.data < current2.data:
            current1 = current1.next
        elif current2.data < current1.data:
            current2 = current2.next

    return new_ll


'''
Approach 2 : Using Hashing
Complexities:
    Time Complexity: O(n)
    Space Complexity: O(m) : where m is lenght of any one of list which you insert in hash
'''
def get_intersection(linked_list_1, linked_list_2):
    new_ll = LinkedList()
    hashmap = {}

    current = linked_list_1.head
    while current:
        hashmap[current.data] = 1
        current = current.next

    current = linked_list_2.head
    while current:
        if hashmap.get(current.data, None):
            new_ll.insert_at_end(current.data)
        current = current.next

    return new_ll  

ll1 = LinkedList([1,2,3,4,5,6])
ll2 = LinkedList([2,4,6])

new_ll = get_intersection(ll1, ll2)
new_ll.traverse()

