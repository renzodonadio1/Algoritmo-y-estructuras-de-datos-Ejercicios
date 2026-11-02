class BinaryTree:
    def __init__(self, value=None, data=None):
        self.value = value
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, value, data=None):
    if root is None:
        return BinaryTree(value, data)
    elif value < root.value:
        root.left = insert_node(root.left, value, data)
    elif value > root.value:
        root.right = insert_node(root.right, value, data)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    elif value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)

def inorden(root):
    if root is not None:
        inorden(root.left)
        print(root.data)
        inorden(root.right)

def por_nivel(root):
    if root is None:
        return
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)