from sorted_doubly_linked_list import SortedDoublyLinkedList


# Example usage:
dll = SortedDoublyLinkedList()
dll.insert("Element 0", 5)
dll.insert("Element 1", 3)
dll.insert("Element 2", 7)
dll.insert("Element 3", 4)

dll.display()

print("Dequeued:", dll.dequeue())
dll.display()

print("Dequeued:", dll.dequeue())
dll.display()
