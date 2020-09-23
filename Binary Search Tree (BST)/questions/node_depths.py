"""
Node Depths:

The distance between a node in a Binary Tree and the tree's root is called
the node's depth.Write a function that takes in a Binary Tree and
returns the sum of its nodes' depths.
"""


def nodeDepths(root, depth=0):
    if root is None:
        return 0

    return depth + nodeDepths(root.left,  depth+1) + nodeDepths(root.right, depth+1)


# This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

"""
Example:

Input:
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9

Output: 16
// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..
// Summing all of these depths yields 16.
"""
