import unittest
import sys
import os

# Adjust path to import from the sibling directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from algorithms.searching import linear_search, binary_search_iterative, binary_search_recursive
from algorithms.graphs import bfs, dfs_iterative, dfs_recursive


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted = [64, 34, 25, 12, 22, 11, 90]
        self.sorted = [11, 12, 22, 25, 34, 64, 90]
        self.empty = []
        self.single = [1]
        self.duplicates = [3, 1, 2, 1, 3, 2]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.unsorted.copy()), self.sorted)
        self.assertEqual(bubble_sort(self.empty.copy()), [])
        self.assertEqual(bubble_sort(self.single.copy()), [1])
        self.assertEqual(bubble_sort(self.duplicates.copy()), [1, 1, 2, 2, 3, 3])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsorted.copy()), self.sorted)
        self.assertEqual(insertion_sort(self.empty.copy()), [])
        self.assertEqual(insertion_sort(self.single.copy()), [1])
        self.assertEqual(insertion_sort(self.duplicates.copy()), [1, 1, 2, 2, 3, 3])

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsorted), self.sorted)
        self.assertEqual(merge_sort(self.empty), [])
        self.assertEqual(merge_sort(self.single), [1])
        self.assertEqual(merge_sort(self.duplicates), [1, 1, 2, 2, 3, 3])

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.unsorted), self.sorted)
        self.assertEqual(quick_sort(self.empty), [])
        self.assertEqual(quick_sort(self.single), [1])
        self.assertEqual(quick_sort(self.duplicates), [1, 1, 2, 2, 3, 3])


class TestSearchingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.arr = [11, 12, 22, 25, 34, 64, 90]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.arr, 22), 2)
        self.assertEqual(linear_search(self.arr, 11), 0)
        self.assertEqual(linear_search(self.arr, 90), 6)
        self.assertIsNone(linear_search(self.arr, 100))

    def test_binary_search_iterative(self):
        self.assertEqual(binary_search_iterative(self.arr, 22), 2)
        self.assertEqual(binary_search_iterative(self.arr, 11), 0)
        self.assertEqual(binary_search_iterative(self.arr, 90), 6)
        self.assertIsNone(binary_search_iterative(self.arr, 100))

    def test_binary_search_recursive(self):
        self.assertEqual(binary_search_recursive(self.arr, 22), 2)
        self.assertEqual(binary_search_recursive(self.arr, 11), 0)
        self.assertEqual(binary_search_recursive(self.arr, 90), 6)
        self.assertIsNone(binary_search_recursive(self.arr, 100))


class TestGraphAlgorithms(unittest.TestCase):
    def setUp(self):
        # A simple graph:
        # A -> B, C
        # B -> D, E
        # C -> F
        # D, E, F have no outgoing edges
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': []
        }

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, 'A'), ['A', 'B', 'C', 'D', 'E', 'F'])
        self.assertEqual(bfs(self.graph, 'C'), ['C', 'F'])
        self.assertEqual(bfs(self.graph, 'Z'), [])

    def test_dfs_iterative(self):
        self.assertEqual(dfs_iterative(self.graph, 'A'), ['A', 'B', 'D', 'E', 'C', 'F'])
        self.assertEqual(dfs_iterative(self.graph, 'C'), ['C', 'F'])
        self.assertEqual(dfs_iterative(self.graph, 'Z'), [])

    def test_dfs_recursive(self):
        self.assertEqual(dfs_recursive(self.graph, 'A'), ['A', 'B', 'D', 'E', 'C', 'F'])
        self.assertEqual(dfs_recursive(self.graph, 'C'), ['C', 'F'])
        self.assertEqual(dfs_recursive(self.graph, 'Z'), [])


if __name__ == '__main__':
    unittest.main()
