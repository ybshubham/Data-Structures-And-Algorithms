from doubly_linked_list import DoublyLinkedList, Node

# def merge_sorted_dlls(dll1, dll2):
#     if not dll1.head and not dll2.head:
#         return None
#     elif not dll1.head:
#         return dll2
#     elif not dll2.head:
#         return dll1
    
#     sorted_dll = DoublyLinkedList()
#     temp = None
#     current1 = dll1.head
#     current2 = dll2.head

#     while current1 and current2:
#         node1 = None
#         node2 = None

#         if current1.data < current2.data:
#             node1 = Node(current1.data)
#             current1 = current1.next
#         elif current1.data > current2.data:
#             node1 = Node(current2.data)
#             current2 = current2.next
#         else:
#             node1 = Node(current1.data)
#             node2 = Node(current2.data)
#             current1 = current1.next
#             current2 = current2.next

#         if node1 and node2:
#             if not temp:
#                 sorted_dll.head = node1
#                 temp = sorted_dll.head
#                 temp.next = node2
#                 node2.prev = temp
#             else:
#                 temp.next = node1
#                 node1.prev = temp
#                 temp = temp.next

#                 temp.next = node2
#                 node2.prev = temp
#                 temp = temp.next
#         else:
#             if not sorted_dll.head:
#                 sorted_dll.head = node1
#                 temp = sorted_dll.head
#             else:
#                 temp.next = node1
#                 node1.prev = temp
#                 temp = temp.next
        
#     while current1:
#         node = Node(current1.data)
#         temp.next = node
#         node.prev = temp
#         temp = temp.next

#         current1 = current1.next

#     while current2:
#         node = Node(current2.data)
#         temp.next = node
#         node.prev = temp
#         temp = temp.next

#         current2 = current2.next

#     return sorted_dll


def merge_sorted_dlls(dll1, dll2):
    if not dll1.head:
        return dll2
    elif not dll2.head:
        return dll1

    merged_dll = DoublyLinkedList()

    current1 = dll1.head
    current2 = dll2.head

    while current1 and current2:
        if current1.data <= current2.data:
            merged_dll.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_dll.insert_at_end(current2.data)
            current2 = current2.next

    # If any list has remaining elements, append them
    while current1:
        merged_dll.insert_at_end(current1.data)
        current1 = current1.next

    while current2:
        merged_dll.insert_at_end(current2.data)
        current2 = current2.next

    return merged_dll

dll1 = DoublyLinkedList([1,3])
dll2 = DoublyLinkedList([2,4,6])

merged_dll = merge_sorted_dlls(dll1, dll2)
if merged_dll:
    merged_dll.forward_traversal()
else:
    print("please provide valid dlls to merge")