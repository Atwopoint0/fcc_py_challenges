class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(node, key):
    if node is None or node.key == key:
        return node
    if node.key < key:
        return search(node.right, key)
    elif node.key  > key:
        return search(node.left, key)
    
def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

    
def insert(node, key):
    if node is None:
        return TreeNode(key)
    if node.val < key:
        node.right = insert(node.right, key)
    elif node.val > key:
        node.left = insert(node.left, key)
    return node

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def delete(node, x):
    if node is None:
        return node
    if node.key > x:
        node.left = delete(node.left, x)
    elif node.key < x:
        node.right = delete(node.right, x)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        if node.right is None:
            temp = node.left
            node = None
            return temp
        node.data = min_value(node.right).data
        node.right = delete(node.right, node.data)     
    return node
