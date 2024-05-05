from ArrayQueue import ArrayQueue


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)

    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if ((root.left is None) and (root.right is None)):
                return 0
            elif (root.right is None):  # left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif (root.left is None):  # right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else:  # both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if self.is_empty():
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)

    def breadth_first(self):
        if (self.is_empty()):
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while (bfs_queue.is_empty() == False):
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                bfs_queue.enqueue(curr_node.left)
            if (curr_node.right is not None):
                bfs_queue.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    def iterative_inorder(self):
        cur = self.root
        while cur is not None:
            if cur.left is None:
                yield cur.data
                cur = cur.right
            else:
                tmp = cur.left
                while (tmp.right is not None) and (tmp.right is not cur):
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None
                    yield cur.data
                    cur = cur.right


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
    for i in tree_1.iterative_inorder():
        print(i, end=' ')

# main()
