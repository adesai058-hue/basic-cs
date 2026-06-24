"""
Singly Linked List Implementation.

A linked list is a linear data structure where elements are not stored 
at contiguous memory locations. Instead, elements are linked using pointers.
"""

from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Node(Generic[T]):
    """A node in a singly linked list."""
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional[Node[T]] = None


class SinglyLinkedList(Generic[T]):
    """Singly Linked List class."""
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None

    def insert_at_head(self, data: T) -> None:
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data: T) -> None:
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data: T) -> bool:
        """
        Delete the first node containing the specified data.
        Returns True if successful, else False.
        """
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
            return True
        return False

    def search(self, data: T) -> bool:
        """Check if data is present in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self) -> List[T]:
        """Convert linked list elements into a standard python list."""
        elements: List[T] = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __str__(self) -> str:
        """String representation of the linked list."""
        elements = self.to_list()
        return " -> ".join(map(str, elements)) + " -> None" if elements else "Empty List"
