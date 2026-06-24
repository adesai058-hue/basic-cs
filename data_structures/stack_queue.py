"""
Stack and Queue Implementations.

- Stack: LIFO (Last In First Out)
- Queue: FIFO (First In First Out)
"""

from typing import TypeVar, Generic, List, Optional
from collections import deque

T = TypeVar('T')

class Stack(Generic[T]):
    """
    LIFO Stack implementation using a dynamic array (Python List).
    All primary operations are O(1) amortized.
    """
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._items)

    def __str__(self) -> str:
        return f"Stack(top={self._items[-1] if not self.is_empty() else None}, size={self.size()})"


class Queue(Generic[T]):
    """
    FIFO Queue implementation using collections.deque for O(1) enqueues and dequeues.
    """
    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> T:
        """Return the front item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._items)

    def __str__(self) -> str:
        return f"Queue(front={self._items[0] if not self.is_empty() else None}, size={self.size()})"
