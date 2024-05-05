from LinkedBinaryTree import *
from ArrayQueue import *


def invert_bt(root: LinkedBinaryTree.Node):
    # Non-Recursive
    if root is None:
        return
    q = ArrayQueue()
    q.enqueue(root)
    while not q.is_empty():
        tmp = q.dequeue()
        if (tmp.left is not None) & (tmp.right is not None):
            tmp.left, tmp.right = tmp.right, tmp.left
            q.enqueue(tmp.left)
            q.enqueue(tmp.right)
        elif tmp.left is not None:
            q.enqueue(tmp.left)
        elif tmp.right is not None:
            q.enqueue(tmp.right)


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
