from sorted_doubly_linked_list import SortedDoublyLinkedList
from rand import RandomNumberGenerator

TIMESTAMP_PER_SECOND = 1e9  # Nanosecond Timestamp

# Example usage:
rng = RandomNumberGenerator()
rate = 150000 / TIMESTAMP_PER_SECOND

dll = SortedDoublyLinkedList()

# Generate 10 random numbers from an exponential distribution
for i in range(10):
    dll.insert(f"Element {i}", rng.exponential(rate))

dll.display()

print("Dequeued:", dll.dequeue())
dll.display()

print("Dequeued:", dll.dequeue())
dll.display()
