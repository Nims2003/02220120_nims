# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def height(self):
        def _height(node):
            return 0 if not node else 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def size(self):
        def _size(node):
            return 0 if not node else 1 + _size(node.left) + _size(node.right)
        return _size(self.root)

    def count_leaves(self):
        def _count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)

    def is_full_binary_tree(self):
        def _full(node):
            if not node:
                return True
            if bool(node.left) != bool(node.right):
                return False
            return _full(node.left) and _full(node.right)
        return _full(self.root)

    def is_complete_binary_tree(self):
        if not self.root:
            return True
        queue = [(self.root, 0)]
        for i, (node, idx) in enumerate(queue):
            if node:
                queue.append((node.left, 2 * idx + 1))
                queue.append((node.right, 2 * idx + 2))
        return queue[-1][1] == len(queue) - 1
# Demonstration
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Tree Height:", tree.height())
    print("Total Nodes:", tree.size())
    print("Leaf Nodes Count:", tree.count_leaves())
    print("Is Full Binary Tree:", tree.is_full_binary_tree())
    print("Is Complete Binary Tree:", tree.is_complete_binary_tree())
