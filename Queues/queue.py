# Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, value):
        # add item to the queue
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        # remove head element from the queue

        if self.head == None:
            return None
        else:
            head_node = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return head_node.value

    def peek(self):
        return self.head.value

# Testing


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

#  Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
