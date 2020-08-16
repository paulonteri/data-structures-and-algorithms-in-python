class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = Node(value)
            else:
                self._insert(value, curr_node.left)
        else:
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:
                self._insert(value, curr_node.right)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node is not None:
            self._print_tree(curr_node.left)
            print(curr_node.value)
            self._print_tree(curr_node.right)

    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, start_node, value):
        if start_node.value == value:
            return True
        elif value < start_node.value:
            if start_node.left is None:
                return False
            else:
                return self._search(start_node.left, value)
        elif value > start_node.value:
            if start_node.right is None:
                return False
            else:
                return self._search(start_node.right, value)


# Fill tree with data
def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for i in range(num_elems):
        elem = randint(0, max_int)
        tree.insert(elem)
    return tree


my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(1)
my_tree.insert(15)
my_tree.insert(5)
my_tree.insert(20)
print(my_tree.search(1))
print(my_tree.search(2))
print(my_tree.search(5))
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(">>>>>>>>>>>>>>>>>>>>>")
my_tree.print_tree()
