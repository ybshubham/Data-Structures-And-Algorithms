from linked_list import LinkedList, Node


'''
Approach 1: Using two for loops
Complexities:
    - Time Complexity : O(n * m) - where n : length of LL1, m: length of LL2
    - Space Complexity: O(1)
'''
# def get_intersection(linked_list_1, linked_list_2):
#     current1 = linked_list_1.head
#     while current1:
#         current2 = linked_list_2.head
#         while current2:
#             if current2 == current1:
#                 return current2
#             current2 = current2.next
#         current1 = current1.next
#     return None


'''
Approach 2: Use hashset (i.e. Set)
Complexities:
    - Time Complexity : O(n + m) - where n : length of LL1, m: length of LL2
    - Space Complexity: O(n) or O(m)
'''
# def get_intersection(linked_list_1, linked_list_2):
#     hashset = set()
#     current = linked_list_1.head
#     while(current):
#         hashset.add(current)
#         current = current.next
    
#     current = linked_list_2.head
#     while(current):
#         if current in hashset:
#             return current
#         current = current.next
#     return None


'''
Approach 3: Use extra node & point every node to it
Complexities:
    - Time Complexity : O(n + m) - where n : length of LL1, m: length of LL2
    - Space Complexity: O(1)
'''
# def get_intersection(linked_list_1, linked_list_2):
#     temp_node = Node()

#     current = linked_list_1.head
#     while(current):
#         next = current.next
#         current.next = temp_node
#         current = next
    
#     current = linked_list_2.head
#     while(current):
#         next = current.next
#         if current.next == temp_node:
#             return current
#         current.next = temp_node
#         current = next
    
#     return None


'''
Approach 4: Modify node structure : 
    Node : {
        data: integer,
        next: pointer to next node,
        visited: Boolean - to check if node is already visited
    }
Complexities:
    - Time Complexity : O(n + m) - where n : length of LL1, m: length of LL2
    - Space Complexity: O(1)
'''
# TODO - write logic

'''
Approach 5: Use two pointer technique
Complexities:
    - Time Complexity : O(n + m) - where n : length of LL1, m: length of LL2
    - Space Complexity: O(1)
'''
# def get_intersection(linked_list_1, linked_list_2):
#     ptr1 = linked_list_1.head
#     ptr2 = linked_list_2.head

#     if ptr1 is None or ptr2 is None:
#         return None

#     while ptr1 != ptr2:
#         ptr1 = ptr1.next
#         ptr2 = ptr2.next

#         if ptr1 == ptr2:
#             return ptr1

#         if ptr1 == None:
#             ptr1 = linked_list_2.head
            
#         elif ptr2 == None:
#             ptr2 = linked_list_1.head

#     return ptr1


'''
Approach 6: Difference in node counts
Complexities:
    - Time Complexity : O(n + m) - where n : length of LL1, m: length of LL2
    - Space Complexity: O(1)
'''
def _find_intersection(diff, ll1, ll2):
    current1 = ll1.head
    while diff:
        current1 = current1.next
        diff -= 1
    
    current2 = ll2.head

    while current1 and current2:
        if current1 == current2:
            return current1
        
        current1 = current1.next
        current2 = current2.next
    return None

def get_intersection(linked_list_1, linked_list_2):
    len1 = linked_list_1.get_length()
    len2 = linked_list_2.get_length()

    if len1 > len2:
        difference = len1 - len2
        return _find_intersection(difference, linked_list_1, linked_list_2)
    else:
        difference = len2 - len1
        return _find_intersection(difference, linked_list_2, linked_list_1)
\
# creating intersected Linked List
ll1 = LinkedList([1,2,3,4,5])
ll2 = LinkedList([1])

third_node = None
current = ll1.head
while current.data != 4:
    current = current.next
third_node = current

temp = ll2.head
while temp.next:
    temp = temp.next
temp.next = third_node

intersection_node = get_intersection(ll1, ll2)
if intersection_node:
    print("Intersection point of two linked lists is:", intersection_node.data)
else:
    print("Given linked lists do not intesect")