class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None

# Demonstration
if __name__ == "__main__":
    tree = BinaryTree()
    print("Created new Binary Tree")
    if tree.root:
        print(f"Root: {tree.root.value}")
    else:
        print("Root: None")
