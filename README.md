# Basic Computer Science Repository (Python)

Welcome to the **Basic CS Repository**! This repository serves as a educational resource and clean implementation guide for fundamental computer science data structures, algorithms, and complexity analysis. All code is implemented in Python with type annotations, docstrings, and comprehensive unit tests.

---

## 📊 Big-O Complexity Cheat Sheet

Here is a summary of the time and space complexities for the structures and algorithms implemented in this repository.

| Data Structure / Algorithm | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Worst) |
| :--- | :--- | :--- | :--- | :--- |
| **Singly Linked List** | | | | |
| - Access / Search | $O(n)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| - Insertion / Deletion | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| **Stack & Queue** | | | | |
| - Push / Enqueue / Pop / Dequeue | $O(1)$ | $O(1)$ | $O(1)$ | $O(n)$ total space |
| **Binary Search Tree** | | | | |
| - Search / Insertion | $O(\log n)$ | $O(\log n)$ | $O(n)$ (unbalanced) | $O(n)$ |
| **Sorting** | | | | |
| - Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| - Insertion Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| - Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| - Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(n)$ |
| **Searching** | | | | |
| - Linear Search | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| - Binary Search | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ iterative, $O(\log n)$ recursive |
| **Graph Traversal** | | | | |
| - Breadth-First Search (BFS) | - | $O(V + E)$ | $O(V + E)$ | $O(V)$ |
| - Depth-First Search (DFS) | - | $O(V + E)$ | $O(V + E)$ | $O(V)$ |

---

## 📂 Repository Structure

```
basic-cs/
├── README.md                  # This educational guide
├── requirements.txt           # Dependency file (uses standard library + pytest)
├── algorithms/
│   ├── sorting.py             # Bubble, Insertion, Merge, Quick Sort
│   ├── searching.py           # Linear & Binary Search
│   └── graphs.py              # BFS & DFS Graph Traversal
├── data_structures/
│   ├── linked_list.py         # Singly Linked List
│   ├── stack_queue.py         # Stack & Queue wrappers
│   └── binary_search_tree.py  # Binary Search Tree (BST)
└── tests/
    ├── test_algorithms.py     # Unit tests for algorithms
    └── test_data_structures.py # Unit tests for data structures
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher.

### Installation

No heavy dependencies are required. However, if you'd like to use `pytest` to run tests:

```bash
pip install -r requirements.txt
```

### Running Tests

You can run the test suite using Python's built-in `unittest` runner:

```bash
python3 -m unittest discover -s tests
```

Or with `pytest` if installed:

```bash
pytest tests/
```

---

## 💡 Topics Covered

### 1. Data Structures
- **Singly Linked List**: A chain of nodes where each node contains data and a reference to the next node. Allows for fast insertions/deletions.
- **Stack (LIFO)**: Last-In, First-Out sequence where elements are added (`push`) and removed (`pop`) from the same end.
- **Queue (FIFO)**: First-In, First-Out sequence where elements are added (`enqueue`) to the back and removed (`dequeue`) from the front.
- **Binary Search Tree (BST)**: A hierarchical node-based structure that maintains sorted keys for fast lookup, insertion, and traversal.

### 2. Algorithms
- **Sorting**:
  - **Bubble Sort & Insertion Sort**: Easy to understand $O(n^2)$ sorting methods.
  - **Merge Sort & Quick Sort**: Highly efficient divide-and-conquer $O(n \log n)$ algorithms.
- **Searching**:
  - **Linear Search**: Scanning each item sequentially.
  - **Binary Search**: Divide-and-conquer strategy on sorted lists.
- **Graph Traversal**:
  - **Breadth-First Search (BFS)**: Explores node by node level-by-level (using a queue).
  - **Depth-First Search (DFS)**: Explores deep along each branch before backtracking (using a stack/recursion).
