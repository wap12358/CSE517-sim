class Node:
    """
    Node class for a doubly linked list, representing each element with a timestamp.
    """
    def __init__(self, event, timestamp):
        self.event = event
        self.timestamp = timestamp
        self.prev = None
        self.next = None

class SortedDoublyLinkedList:
    """
    Doubly linked list class with sorted insertions based on timestamps.
    Elements are inserted in ascending order of timestamp.
    The smallest timestamp element is removed first when dequeued.
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None and self.tail == None

    def insert(self, event, timestamp):
        """
        Inserts a new node with event and timestamp in ascending order based on timestamp.
        """
        new_node = Node(event, timestamp)
        
        # Case: List is empty
        if not self.head:
            self.head = self.tail = new_node
            return
        
        # Case: Insert at the beginning if new timestamp is smallest
        if timestamp < self.head.timestamp:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        # Case: Insert at the end if new timestamp is largest
        if timestamp >= self.tail.timestamp:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        # Case: Insert in the middle
        current = self.head
        while current and current.timestamp <= timestamp:
            current = current.next
        previous_node = current.prev

        # Insert between previous_node and current
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = current
        current.prev = new_node

    def dequeue(self):
        """
        Removes and returns the element with the smallest timestamp.
        """
        if not self.head:
            return None  # List is empty

        smallest_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return smallest_node.event, smallest_node.timestamp

    def display(self):
        """
        Displays all elements in the list from head to tail with their timestamps.
        """
        elements = []
        current = self.head
        while current:
            elements.append((str(current.event), current.timestamp))
            current = current.next
        print("List:", elements)
