"""
Binary Search Tree (BST) Implementation.

A Binary Search Tree is a node-based binary tree data structure which has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- The left and right subtree must each also be a binary search tree.
"""

from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class BSTNode(Generic[T]):
    """A node in a Binary Search Tree."""
    def __init__(self, key: T) -> None:
        self.key: T = key
        self.left: Optional[BSTNode[T]] = None
        self.right: Optional[BSTNode[T]] = None


class BinarySearchTree(Generic[T]):
    """Binary Search Tree Class."""
    def __init__(self) -> None:
        self.root: Optional[BSTNode[T]] = None

    def insert(self, key: T) -> None:
        """Insert a key into the BST."""
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: BSTNode[T], key: T) -> None:
        if key < node.key:
            if not node.left:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if not node.right:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key: T) -> bool:
        """Search for a key in the BST. Returns True if found, else False."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[BSTNode[T]], key: T) -> bool:
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self) -> List[T]:
        """In-order traversal: Left -> Root -> Right (produces sorted order)."""
        result: List[T] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[BSTNode[T]], result: List[T]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self) -> List[T]:
        """Pre-order traversal: Root -> Left -> Right."""
        result: List[T] = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[BSTNode[T]], result: List[T]) -> None:
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self) -> List[T]:
        """Post-order traversal: Left -> Right -> Root."""
        result: List[T] = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[BSTNode[T]], result: List[T]) -> None:
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
