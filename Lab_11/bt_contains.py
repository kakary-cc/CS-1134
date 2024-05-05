from LinkedBinaryTree import *


def bt_contains(root: LinkedBinaryTree.Node, val):
    if root is None:
        return False
    if root.data == val:
        return True
    return bt_contains(root.left, val) | bt_contains(root.right, val)


def main():
    n_9 = LinkedBinaryTree.Node(9)
    n_11 = LinkedBinaryTree.Node(11)
    n_1 = LinkedBinaryTree.Node(1, n_9, n_11)
    n_4 = LinkedBinaryTree.Node(4)
    n_6 = LinkedBinaryTree.Node(6, n_1, n_4)
    n_3 = LinkedBinaryTree.Node(3)
    n_7 = LinkedBinaryTree.Node(7, n_3, n_6)
    bt = LinkedBinaryTree(n_7)
    for i in [9, 11, 1, 4, 6, 3, 7]:
        print(bt_contains(bt.root, i), end=' ')
    print()
    for i in [2, 5, 8, 12, 16]:
        print(bt_contains(bt.root, i), end=' ')
        