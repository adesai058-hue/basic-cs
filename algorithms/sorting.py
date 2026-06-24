"""
Sorting Algorithms Implementation.

This module provides standard implementations of sorting algorithms:
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
"""

from typing import List, TypeVar

T = TypeVar('T')

def bubble_sort(arr: List[T]) -> List[T]:
    """
    Sorts a list in place using Bubble Sort.
    
    Time Complexity:
        Best: O(n) - list is already sorted
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity: O(1) auxiliary
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr: List[T]) -> List[T]:
    """
    Sorts a list in place using Insertion Sort.
    
    Time Complexity:
        Best: O(n) - list is already sorted
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity: O(1) auxiliary
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List[T]) -> List[T]:
    """
    Sorts and returns a new list using Merge Sort.
    
    Time Complexity:
        Best/Average/Worst: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[T], right: List[T]) -> List[T]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: List[T]) -> List[T]:
    """
    Sorts and returns a new list using Quick Sort (out-of-place version for clarity).
    
    Time Complexity:
        Best/Average: O(n log n)
        Worst: O(n^2)
    Space Complexity: O(n) (due to call stack and partitioned arrays)
    """
    if len(arr) <= 1:
        return arr
    
    # Choose midpoint as pivot to avoid O(n^2) on sorted/reverse sorted inputs
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
