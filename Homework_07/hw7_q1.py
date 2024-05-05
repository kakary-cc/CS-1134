from LinkedBinaryTree import *


def min_and_max(bin_tree: LinkedBinaryTree):
    def subtree_min_and_max(root: LinkedBinaryTree.Node):
        if root is None:
            return (None, None)
        else:
            left_mm = subtree_min_and_max(root.left)
            right_mm = subtree_min_and_max(root.right)
            min_val = [left_mm[0], right_mm[0], root.data]
            min_val = [i for i in min_val if i is not None]
            max_val = [left_mm[1], right_mm[1], root.data]
            max_val = [i for i in max_val if i is not None]
            return (min(min_val), max(max_val))

    if bin_tree.root is None:
        raise Exception('Empty Tree.')
    return subtree_min_and_max(bin_tree.root)


def main():
    n5 = LinkedBinaryTree.Node(5)
    n1 = LinkedBinaryTree.Node(1)
    n9 = LinkedBinaryTree.Node(9, n5, n1)
    n2 = LinkedBinaryTree.Node(2, n9)
    n8 = LinkedBinaryTree.Node(8)
    n4 = LinkedBinaryTree.Node(4)
    n7 = LinkedBinaryTree.Node(7, n8, n4)
    n3 = LinkedBinaryTree.Node(3, n2, n7)
    tree_1 = LinkedBinaryTree(n3)
    print(min_and_max(tree_1))

    tree_2 = LinkedBinaryTree(None)
    print(min_and_max(tree_2))