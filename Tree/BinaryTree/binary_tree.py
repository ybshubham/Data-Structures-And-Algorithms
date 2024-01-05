class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    #Searching for an element
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or key == root.key:
            return root
    
        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)


    #Inserting an element
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
    
        # doesn't add duplicate node
        return root

    #Removing an element
    #Deletion for an element
    def remove_node(self):
        pass

    #Traversing an element
    def preorder_traversal(self):
        pass

    def inorder_traversal(self):
        pass

    def postorder_traversal(self):
        pass

    # find height
    def get_height(self):
        pass

    # find level
    def get_level(self):
        pass

    # find size
    def get_size(self):
        pass
