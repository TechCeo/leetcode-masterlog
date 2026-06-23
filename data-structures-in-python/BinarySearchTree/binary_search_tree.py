"""
Binary Search Tree
------------------

For every node in a binary search tree (BST), smaller values are stored in its
left subtree and larger values in its right subtree. This implementation keeps
values unique.

Average Complexity:
- Search, insert, remove: O(log n)

Worst Case:
- O(n) when insertion order makes the tree highly unbalanced

An in-order traversal of a BST visits values in sorted order.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def is_empty(self) -> bool:
        return self.root is None

    def size(self) -> int:
        return self._size

    def insert(self, value) -> bool:
        """Insert a unique value. Return False when it already exists."""
        if self.root is None:
            self.root = TreeNode(value)
            self._size = 1
            return True

        current = self.root
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                current = current.right

        self._size += 1
        return True

    def contains(self, value) -> bool:
        current = self.root

        while current:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right

        return False

    def remove(self, value) -> bool:
        """Remove a value while preserving the BST ordering rule."""
        self.root, removed = self._remove(self.root, value)
        if removed:
            self._size -= 1
        return removed

    def _remove(self, node, value):
        if node is None:
            return None, False

        if value < node.value:
            node.left, removed = self._remove(node.left, value)
            return node, removed
        if value > node.value:
            node.right, removed = self._remove(node.right, value)
            return node, removed

        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Replace a two-child node with its in-order successor.
        successor = node.right
        while successor.left:
            successor = successor.left

        node.value = successor.value
        node.right, _ = self._remove(node.right, successor.value)
        return node, True

    def inorder(self) -> list:
        values = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            values.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return values

    def preorder(self) -> list:
        values = []

        def traverse(node):
            if node is None:
                return
            values.append(node.value)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return values

    def postorder(self) -> list:
        values = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            values.append(node.value)

        traverse(self.root)
        return values

    def __repr__(self) -> str:
        return f"BinarySearchTree({self.inorder()})"


if __name__ == "__main__":
    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        assert tree.insert(value)

    assert not tree.insert(6)
    assert tree.contains(7)
    assert not tree.contains(12)
    assert tree.inorder() == [1, 3, 4, 6, 7, 8, 10, 13, 14]

    assert tree.remove(1)   # Leaf
    assert tree.remove(14)  # One child
    assert tree.remove(3)   # Two children
    assert not tree.remove(99)
    assert tree.inorder() == [4, 6, 7, 8, 10, 13]
    assert tree.size() == 6

    print("All binary_search_tree tests passed.")
