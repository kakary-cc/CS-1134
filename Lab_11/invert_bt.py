from LinkedBinaryTree import *


def invert_bt(root: LinkedBinaryTree.Node):
    # Recursive
    if root is None:
        return
    invert_bt(root.left)
    invert_bt(root.right)
    root.left, root.right = root.right, root.left


def main():
    n_9 = LinkedBinaryTree.Node(9)
    n_11 = LinkedBinaryTree.Node(11)
    n_1 = LinkedBinaryTree.Node(1, n_9, n_11)
    n_4 = LinkedBinaryTree.Node(4)
    n_6 = LinkedBinaryTree.Node(6, n_1, n_4)
    n_3 = LinkedBinaryTree.Node(3)
    n_7 = LinkedBinaryTree.Node(7, n_3, n_6)
    bt = LinkedBinaryTree(n_7)
    invert_bt(bt.root)
    for i in bt:
        print(i, end=' ')
