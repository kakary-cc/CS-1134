from LinkedBinaryTree import *


def is_height_balanced(bin_tree: LinkedBinaryTree):

    def subtree_ihb(root: LinkedBinaryTree.Node):
        if (root.left is None) and (root.right is None):
            return (0, 0)
        elif root.right is None:
            left_height = subtree_ihb(root.left)
            if left_height is False:
                return False
            left_height = left_height[0]
            if left_height > 0:
                return False
            return (1 + left_height, 0)
        elif root.left is None:
            right_height = subtree_ihb(root.right)
            if right_height is False:
                return False
            right_height = right_height[1]
            if right_height > 0:
                return False
            return (0, 1 + right_height)
        else:
            left_height = subtree_ihb(root.left)
            if left_height is False:
                return False
            left_height = left_height[0]
            right_height = subtree_ihb(root.right)
            if right_height is False:
                return False
            right_height = right_height[1]
            if abs(left_height - right_height) > 1:
                return False
            return (1 + left_height, 1 + right_height)

    if bin_tree.root is None:
        return True
    if not subtree_ihb(bin_tree.root):
        return False
    return True


def main():
    # n5 = LinkedBinaryTree.Node(5)
    # n1 = LinkedBinaryTree.Node(1)
    # n9 = LinkedBinaryTree.Node(9, n5, n1)
    # n2 = LinkedBinaryTree.Node(2, n9)
    # n8 = LinkedBinaryTree.Node(8)
    # n4 = LinkedBinaryTree.Node(4)
    # n7 = LinkedBinaryTree.Node(7, n8, n4)
    # n3 = LinkedBinaryTree.Node(3, n2, n7)
    # tree_1 = LinkedBinaryTree(n3)
    # print(is_height_balanced(tree_1))

    n5 = LinkedBinaryTree.Node(5)
    n1 = LinkedBinaryTree.Node(1)
    n9 = LinkedBinaryTree.Node(9, n5, n1)
    n2 = LinkedBinaryTree.Node(2, n9)
    n8 = LinkedBinaryTree.Node(8)
    n4 = LinkedBinaryTree.Node(4)
    n7 = LinkedBinaryTree.Node(7, n8, n4)
    n3 = LinkedBinaryTree.Node(3, n2, n7)
    tree_2 = LinkedBinaryTree(n3)
    print(is_height_balanced(tree_2))


# main()
