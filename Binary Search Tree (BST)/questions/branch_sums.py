"""
Branch Sums:

Write a function that takes in a Binary Tree and
returns a list of its branch sums ordered from
the left most branch sum to the right most branch sum.
"""

def branchSums(root):
	sums_list = []
	branchSumsHelper(root, sums_list, 0)
	return sums_list


def branchSumsHelper(node, sums_list, total):
    # will handle the ones with one None(null) child
	if node is None:
		return

	# add node's value to total
	total += node.value

	# leaf node (main base case)
	if node.left is None and node.right is None:
		# add the total to the sum list
		sums_list.append(total)
		return

    # some recursive fun 🔥🔥🔥
	branchSumsHelper(node.left, sums_list, total)
	branchSumsHelper(node.right, sums_list, total)

# # Binary Tree
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
