# Stack


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def pop(self):
        if self.head:
            popped = self.head.value
            self.head = self.head.next
            return popped
        return None

    def list_data(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values


# Testing
q = Stack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q.list_data())
q.pop()
print(q.list_data())
q.push(7)
print(q.list_data())
