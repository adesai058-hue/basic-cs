"""
Graph Traversal Algorithms Implementation.

This module provides standard implementations of graph traversal algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
"""

from typing import Dict, List, Set, TypeVar, Optional
from collections import deque

T = TypeVar('T')
Graph = Dict[T, List[T]]

def bfs(graph: Graph[T], start: T) -> List[T]:
    """
    Breadth-First Search traversal of a graph starting from a node.
    Returns list of nodes in visited order.
    
    Time Complexity: O(V + E) where V is vertices, E is edges.
    Space Complexity: O(V)
    """
    if start not in graph:
        return []

    visited: Set[T] = {start}
    queue: deque[T] = deque([start])
    order: List[T] = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs_iterative(graph: Graph[T], start: T) -> List[T]:
    """
    Depth-First Search traversal of a graph starting from a node (iterative).
    Returns list of nodes in visited order.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start not in graph:
        return []

    visited: Set[T] = set()
    stack: List[T] = [start]
    order: List[T] = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            # Push neighbors in reverse to traverse in a predictable order
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def dfs_recursive(graph: Graph[T], start: T, visited: Optional[Set[T]] = None) -> List[T]:
    """
    Depth-First Search traversal of a graph starting from a node (recursive).
    Returns list of nodes in visited order.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V) call stack space
    """
    if start not in graph:
        return []
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))

    return order

