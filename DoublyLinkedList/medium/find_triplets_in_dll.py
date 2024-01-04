from doubly_linked_list import DoublyLinkedList

'''
Approach 1: Use 3 nested for loops
Complexities : 
    Time: O(n^3)
    space: O(1)
'''

'''
Approach 2: Use hashmap
Complexities : 
    Time: O(n^2)
    space: O(n)
'''

'''
Approach 3: Use two pointer technique
Complexities : 
    Time: O(n^2)
    space: O(1)
'''
def find_triplets(dll, sum):
    result = []
    if not dll.head:
        return result

    current = dll.head

    while current:
        start = current.next

        if not start:
            break

        end = start.next if start.next else None
        while end and end.next:
            end = end.next

        if not end:
            break

        while start and end and start != end:
            triplet_sum = current.data + start.data + end.data
            if triplet_sum == sum:
                result.append((current.data, start.data, end.data))
            
            if triplet_sum > sum:
                end = end.prev
            else:
                start = start.next

        current = current.next

    return result

dll = DoublyLinkedList([1,2,4,5,6,8,9])
sum = 17

print("Triplets:", find_triplets(dll, sum))