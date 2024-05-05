from LinkedBinaryTree import *


def bt_even_sum(root: LinkedBinaryTree.Node):
    if root is None:
        return 0
    if root.data % 2:
        return bt_even_sum(root.left) + bt_even_sum(root.right)
    else:
        return bt_even_sum(root.left) + bt_even_sum(root.right) + root.data


def main():
    n_9 = LinkedBinaryTree.Node(9)
    n_11 = LinkedBinaryTree.Node(11)
    n_1 = LinkedBinaryTree.Node(1, n_9, n_11)
    n_4 = LinkedBinaryTree.Node(4)
    n_6 = LinkedBinaryTree.Node(6, n_1, n_4)
    n_3 = LinkedBinaryTree.Node(3)
    n_7 = LinkedBinaryTree.Node(7, n_3, n_6)
    bt = LinkedBinaryTree(n_7)
    print(bt_even_sum(bt.root))