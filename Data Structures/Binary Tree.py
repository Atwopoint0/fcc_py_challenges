from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Preorder is useful for making copies of BTs and getting prefix expressions.
def preorder_traversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

# Inorder is useful for non-decreasing ordering in BSTs and evaluating arithmetic expressions.
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=", ")
    inorder_traversal(node.right)

# Postorder is useful for deleting BTs and getting suffix expressions.
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=", ")

# Level order can be used to find shortest paths and is used for tree (de)serialisation.
def level_order_traversal(node):
    if node is None:
        return
    queue = deque([node])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def insert(node, data):
    if node is None:
        node = TreeNode(data)
        return node
    
    # Queue to traverse the tree and find the position to insert the node
    q = deque()
    q.append(node)
    while q:
        temp = q.popleft()
        # Insert node as the left child of the parent node
        if temp.left is None:
            temp.left = TreeNode(data)
            break
        # If the left child is not null push it to the queue
        else:
            q.append(temp.left)
        # Insert node as the right child of parent node
        if temp.right is None:
            temp.right = TreeNode(data)
            break
        # If the right child is not null push it to the queue
        else:
            q.append(temp.right)
    return node

def deletDeepest(root, d_node):
    q = deque()
    q.append(root)
    # Do level order traversal until last node
    while q:
        temp = q.popleft()
        if temp == d_node:
            temp = None
            del d_node
            return
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                del d_node
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                del d_node
                return
            else:
                q.append(temp.left)

# Function to delete element in binary tree
def deletion(node, key):
    if node is None:
        return None
    if node.left is None and node.right is None:
        if node.data == key:
            return None
        else:
            return node
    
    q = deque()
    q.append(node)
    temp = None
    key_node = None
    # Do level order traversal to find deepest node (temp) and node to be deleted (key_node)
    while q:
        temp = q.popleft()
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if key_node is not None:
        x = temp.data
        key_node.data = x
        deletDeepest(node, temp)
    return node