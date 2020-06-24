"""
A linked list is a collection of 'nodes'. 
The first node is called the head, and it’s used as the starting point for any iteration through the list. 
The last node must have its next reference pointing to None to determine the end of the list.
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        current =  self.head
        if self.head:
            # iterate through the next reference in every Node until you reach the end of the list
            while current.next:
                current = current.next
            # set next for the end of the list to be the new_element 
            current.next = new_element
        # if there is no head, you should just assign new_element to it
        else:
            self.head = new_element
            
            
    # deletes by value(not 'index')        
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
                
    def get_position(self, position):
        counter = 0
        current = self.head
        if position < 0:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        counter = 0
        current = self.head
        if position == 0:
            new_element.next = self.head
            self.head = new_element
        elif position > 0:
            while current and counter < position:
                if counter ==  position - 1:
                    new_element.next = current.next 
                    current.next =  new_element
                #
                current = current.next
                counter += 1
    
    # Returns the length of the linked list
    def length(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter
            
    # Prints out the linked list in traditional Python list format
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)
        
    # Deletes the node at index 'position'
    def erase(self, position):
        if position > self.length():
            return print("ERROR: Index out of range!")
        
        if self.head == None: 
            return
        
        counter =  0
        current =  self.head
        
        if position == 0:
            self.head = current.next
            return
            

        while current.next and counter < position:
            previous = current
            current = current.next
            if counter == position - 1:
                previous.next = current.next              
            counter += 1

"""
Testing
"""

# Set up some Nodes
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e5)

# Test Display
print("\nTest Display")
ll.display()

# Test Length 
print("\nTest Length")
print("length is equal to: " + str(ll.length()))

# Test get_position()
print("\nTest get_position()")
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(2).value)


# Test Insert
print("\nTest Insert")
ll.insert(e4,2)
# should print 4 now
print("Should print 4 now")
print(ll.get_position(2).value)


# Test Delete
print("\nTest Delete")
ll.display()
one = ll.get_position(0).value
two = ll.get_position(1).value
three = ll.get_position(2).value
print("Deleting...")
ll.delete(one)
print("Should print: " + str(two))
print(ll.get_position(0).value)
print("Should print: " + str(three))
print(ll.get_position(1).value)
ll.display()

# Test Erase
print("\nTest Erase")
ll.display()
ll.erase(1)
ll.display()
