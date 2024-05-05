from LinkedBinaryTree import *


def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split()
    prefix_exp = prefix_exp[::-1]

    def create_expression_subtree(prefix_exp_str):
        subtree_root = LinkedBinaryTree.Node(prefix_exp.pop())
        if prefix_exp[-1].isdigit():
            subtree_root.left = LinkedBinaryTree.Node(int(prefix_exp.pop()))
        else:
            subtree_root.left = create_expression_subtree(prefix_exp)
        if prefix_exp[-1].isdigit():
            subtree_root.right = LinkedBinaryTree.Node(int(prefix_exp.pop()))
        else:
            subtree_root.right = create_expression_subtree(prefix_exp)
        return subtree_root

    return LinkedBinaryTree(create_expression_subtree(prefix_exp))


def prefix_to_postfix(prefix_exp_str):
    exp_tree = create_expression_tree(prefix_exp_str)

    def postorder_iter(self):
        for node in self.postorder():
            yield str(node.data)

    postfix_exp_str = ' '.join(postorder_iter(exp_tree))
    return postfix_exp_str


# tree = create_expression_tree('* 2 + - 15 6 4')
# print(prefix_to_postfix('* 2 + - 15 6 4'))
