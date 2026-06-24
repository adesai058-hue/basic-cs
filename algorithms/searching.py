"""
Searching Algorithms Implementation.

This module provides standard implementations of searching algorithms:
- Linear Search
- Binary Search (Iterative)
- Binary Search (Recursive)
"""

from typing import List, TypeVar, Optional

T = TypeVar('T')

def linear_search(arr: List[T], target: T) -> Optional[int]:
    """
    Searches for target in list sequentially.
    Returns the index if found, else None.
    
    Time Complexity:
        Best: O(1)
        Average/Worst: O(n)
    Space Complexity: O(1)
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None


def binary_search_iterative(arr: List[T], target: T) -> Optional[int]:
    """
    Searches for target in a sorted list iteratively.
    Returns the index if found, else None.
    
    Time Complexity:
        Best: O(1)
        Average/Worst: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None


def binary_search_recursive(arr: List[T], target: T, low: int = 0, high: Optional[int] = None) -> Optional[int]:
    """
    Searches for target in a sorted list recursively.
    Returns the index if found, else None.
    
    Time Complexity:
        Best: O(1)
        Average/Worst: O(log n)
    Space Complexity: O(log n) call stack space
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
