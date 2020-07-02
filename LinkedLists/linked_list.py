"""
A linked list is a collection of 'nodes'. 
The first node is called the head, and it’s used as the starting point for any iteration through the list. 
The last node must have its next reference pointing to None to determine the end of the list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def print_list(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print(values)

    def length(self):
        # length of list
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def append(self, value):
        # add value to the end of the list
        new_node = Node(value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def prepend(self, value):
        # add value to the beggining of the list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        # delete by value
        if not self.head:
            raise Exception(
                "ERROR: Cannot delete element in an empty Linked List!")
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = self.head.next

    def delete_by_index(self, index):
        # delete by index
        if index > self.length() - 1:
            raise Exception("ERROR: Index out of range!")

        counter = 0
        current = self.head
        prev = None

        if index == 0:
            self.head = current.next
            return

        while current.next and index > counter:
            prev = current
            current = current.next
            if counter == index - 1:
                prev.next = current.next
            counter += 1

    def insert(self, value, index):
        # insert new node at index
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index > 0:
            counter = 0
            current = self.head

            while current.next and counter < index:
                if index - 1 == counter:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1

    def get_index(self, index):
        # get node at index
        if index < 0 or index > self.length() - 1:
            return None

        if index == 0:
            return self.head

        counter = 0
        current = self.head
        while current and counter <= index:
            if index == counter:
                return current
            current = current.next
            counter += 1

        return None


# TESTING
q = LinkedList()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
print("Test Append. Should print: [1, 2, 3, 4, 5, 6]")
print("Test Append:")
q.print_list()

#
print("Length:" + str(q.length()))

#
q.prepend(0)
print("Test prepend. Should print: [0, 1, 2, 3, 4, 5, 6]")
print("Test prepend:")
q.print_list()

#
q.delete_by_value(0)
print("Test delete_by_value. Should print: [1, 2, 3, 4, 5, 6]")
print("Test delete_by_value:")
q.print_list()

#
q.delete_by_index(1)
print("Test delete_by_index. Should print: [1, 3, 4, 5, 6]")
print("Test delete_by_index:")
q.print_list()

#
print("Test get_index. Should print:4")
print("Test get_index: " + str(q.get_index(2).value))
q.print_list()

#
q.insert(2, 1)
print("Test delete_by_index. Should print: [1, 2, 3, 4, 5, 6]")
print("Test delete_by_index:")
q.print_list()
