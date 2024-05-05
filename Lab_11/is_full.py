from LinkedBinaryTree import *


def is_full(root: LinkedBinaryTree.Node):
    if (root.left is None) | (root.right is None):
        if (root.left is None) & (root.right is None):
            return True
        else:
            return False
    return is_full(root.left) & is_full(root.right)


def main():
    n_9 = LinkedBinaryTree.Node(9)
    n_11 = LinkedBinaryTree.Node(11)
    n_1 = LinkedBinaryTree.Node(1, n_9, n_11)
    n_4 = LinkedBinaryTree.Node(4)
    n_6 = LinkedBinaryTree.Node(6, n_1, n_4)
    n_3 = LinkedBinaryTree.Node(3)
    n_7 = LinkedBinaryTree.Node(7, n_3, n_6)
    bt = LinkedBinaryTree(n_7)
    print(is_full(bt.root))

    n_9 = LinkedBinaryTree.Node(9)
    n_11 = LinkedBinaryTree.Node(11)
    n_1 = LinkedBinaryTree.Node(1, n_9)  # Changed here
    n_4 = LinkedBinaryTree.Node(4)
    n_6 = LinkedBinaryTree.Node(6, n_1, n_4)
    n_3 = LinkedBinaryTree.Node(3)
    n_7 = LinkedBinaryTree.Node(7, n_3, n_6)
    bt = LinkedBinaryTree(n_7)
    print(is_full(bt.root))
