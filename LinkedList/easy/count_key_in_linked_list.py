from linked_list import LinkedList

def count_key(linked_list, key):
    current = linked_list.head
    count = 0

    if not current:
        return count
    
    while current:
        if current.data == key:
            count += 1
        current = current.next
    
    return count

ll = LinkedList([1,2,1,2,1,3,1])
key = 1
count = count_key(ll, key)

print(f"{key} has occured {count} times in Linked List")