from binary_tree import BinaryTree

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
'''
Tree:
    5
   / \
  3   7
 / \
2   4
'''

print(tree.search(9))