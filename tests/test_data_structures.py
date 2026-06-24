import unittest
import sys
import os

# Adjust path to import from the sibling directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.linked_list import SinglyLinkedList
from data_structures.stack_queue import Stack, Queue
from data_structures.binary_search_tree import BinarySearchTree


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = SinglyLinkedList()

    def test_insert_and_to_list(self):
        self.assertEqual(self.ll.to_list(), [])
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(1)
        self.ll.insert_at_tail(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])

    def test_search(self):
        self.ll.insert_at_tail(10)
        self.ll.insert_at_tail(20)
        self.assertTrue(self.ll.search(10))
        self.assertTrue(self.ll.search(20))
        self.assertFalse(self.ll.search(30))

    def test_delete(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        
        self.assertTrue(self.ll.delete(2))
        self.assertEqual(self.ll.to_list(), [1, 3])
        
        self.assertTrue(self.ll.delete(1))
        self.assertEqual(self.ll.to_list(), [3])
        
        self.assertFalse(self.ll.delete(100))
        self.assertEqual(self.ll.to_list(), [3])
        
        self.assertTrue(self.ll.delete(3))
        self.assertEqual(self.ll.to_list(), [])
        self.assertFalse(self.ll.delete(3))


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_operations(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.peek(), 20)
        
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.peek(), 10)
        self.assertEqual(self.stack.pop(), 10)
        
        self.assertTrue(self.stack.is_empty())
        with self.assertRaises(IndexError):
            self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_operations(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.peek(), 10)
        
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.peek(), 20)
        self.assertEqual(self.queue.dequeue(), 20)
        
        self.assertTrue(self.queue.is_empty())
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Tree shape:
        #      5
        #    /   \
        #   3     7
        #  / \   / \
        # 2   4 6   8
        self.bst = BinarySearchTree()
        for key in [5, 3, 7, 2, 4, 6, 8]:
            self.bst.insert(key)

    def test_search(self):
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(2))
        self.assertTrue(self.bst.search(8))
        self.assertFalse(self.bst.search(10))
        self.assertFalse(self.bst.search(0))

    def test_inorder(self):
        self.assertEqual(self.bst.inorder_traversal(), [2, 3, 4, 5, 6, 7, 8])

    def test_preorder(self):
        self.assertEqual(self.bst.preorder_traversal(), [5, 3, 2, 4, 7, 6, 8])

    def test_postorder(self):
        self.assertEqual(self.bst.postorder_traversal(), [2, 4, 3, 6, 8, 7, 5])


if __name__ == '__main__':
    unittest.main()
