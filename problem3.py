'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    if not node:
        return '-1'
    return ','.join([node.val, serialize(node.left), serialize(node.right)])


def deserialize(s):
    nodes_value = iter(s.split(','))

    def get_tree():
        root = next(nodes_value)
        if root == '-1':
            return
        return Node(root, get_tree(), get_tree())

    return get_tree()


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = serialize(node)
    assert deserialize(serialize(node)).left.left.val == 'left.left'
