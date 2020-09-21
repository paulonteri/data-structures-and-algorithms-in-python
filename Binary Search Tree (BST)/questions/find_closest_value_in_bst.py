"""
Find Closest Value In BST:

Write a function that takes in a Binary Search Tree (BST)
and a target integer value
and returns the closest value to that target value contained in the BST.
"""

def findClosestValueInBst(tree, target):
	closest = tree.value
	curr = tree

	while curr is not None:
		# check if we should update closest
		if abs(curr.value - target) < abs(closest - target):
			closest = curr.value

		# move on to next
		# either right or left will have a closer value
		if target < curr.value:
			curr = curr.left
		else:
			curr = curr.right

	return closest

# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
