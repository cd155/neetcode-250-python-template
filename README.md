# NeetCode 250 Python Solutions

A collection of solution templates for the "NeetCode 250" LeetCode problems in Python.

## 📚 Overview

This repository contains Python solution templates for the NeetCode 250 list - the NeetCode 150 plus 100 more LeetCode problems, curated by NeetCode to cover the most important patterns and concepts for technical interviews.

Each problem comes with:

- a solution file in `src/<category>/` with the full problem statement, a `TODO` stub, and example usage
- a test file in `tests/` built from the problem's examples (the tests fail until you implement the solution)

## 🗂️ Structure

Solutions are organized by the [NeetCode 250](https://neetcode.io/practice/practice/neetcode250) categories:

```
src/
├── arrays_and_hashing/  # Arrays & Hashing (22)
├── two_pointers/        # Two Pointers (13)
├── sliding_window/      # Sliding Window (9)
├── stack/               # Stack (15)
├── binary_search/       # Binary Search (14)
├── linked_list/         # Linked List (14)
├── trees/               # Trees (23)
├── heap_priority_queue/ # Heap / Priority Queue (12)
├── backtracking/        # Backtracking (16)
├── tries/               # Tries (4)
├── graphs/              # Graphs (21)
├── advanced_graphs/     # Advanced Graphs (10)
├── dp_1d/               # 1-D Dynamic Programming (17)
├── dp_2d/               # 2-D Dynamic Programming (16)
├── greedy/              # Greedy (14)
├── intervals/           # Intervals (7)
├── math_and_geometry/   # Math & Geometry (13)
└── bit_manipulation/    # Bit Manipulation (10)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/cd155/neetcode-250-python-template.git
cd neetcode-250-python-template

# Create python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific problem
pytest tests/test_concatenation_of_array.py

# Run tests for every problem whose name matches a keyword
pytest -k "linked_list"
```

### Running Individual Solutions

Each solution file can be run independently:

```bash
python src/arrays_and_hashing/concatenation_of_array.py
```

### Tracking Progress with GitHub Issues

The **Create NeetCode 250 Issues** workflow opens one issue per problem, labeled `neetcode-250` and
by category. Run it from the repository's **Actions** tab and type `yes` to confirm. Problems that
already have an issue are skipped, so it is safe to run again.

## 📝 Problem Categories

### Arrays & Hashing (22 problems)
- Concatenation of Array (Easy)
- Contains Duplicate (Easy)
- Valid Anagram (Easy)
- Two Sum (Easy)
- Longest Common Prefix (Easy)
- Group Anagrams (Medium)
- Remove Element (Easy)
- Majority Element (Easy)
- Design HashSet (Easy)
- Design HashMap (Easy)
- Sort an Array (Medium)
- Sort Colors (Medium)
- Top K Frequent Elements (Medium)
- Encode and Decode Strings (Medium)
- Range Sum Query 2D - Immutable (Medium)
- Product of Array Except Self (Medium)
- Valid Sudoku (Medium)
- Longest Consecutive Sequence (Medium)
- Best Time to Buy and Sell Stock II (Medium)
- Majority Element II (Medium)
- Subarray Sum Equals K (Medium)
- First Missing Positive (Hard)

### Two Pointers (13 problems)
- Reverse String (Easy)
- Valid Palindrome (Easy)
- Valid Palindrome II (Easy)
- Merge Strings Alternately (Easy)
- Merge Sorted Array (Easy)
- Remove Duplicates from Sorted Array (Easy)
- Two Sum II - Input Array Is Sorted (Medium)
- 3Sum (Medium)
- 4Sum (Medium)
- Rotate Array (Medium)
- Container With Most Water (Medium)
- Boats to Save People (Medium)
- Trapping Rain Water (Hard)

### Sliding Window (9 problems)
- Contains Duplicate II (Easy)
- Best Time to Buy and Sell Stock (Easy)
- Longest Substring Without Repeating Characters (Medium)
- Longest Repeating Character Replacement (Medium)
- Permutation in String (Medium)
- Minimum Size Subarray Sum (Medium)
- Find K Closest Elements (Medium)
- Minimum Window Substring (Hard)
- Sliding Window Maximum (Hard)

### Stack (15 problems)
- Baseball Game (Easy)
- Valid Parentheses (Easy)
- Implement Stack using Queues (Easy)
- Implement Queue using Stacks (Easy)
- Min Stack (Medium)
- Evaluate Reverse Polish Notation (Medium)
- Generate Parentheses (Medium)
- Asteroid Collision (Medium)
- Daily Temperatures (Medium)
- Online Stock Span (Medium)
- Car Fleet (Medium)
- Simplify Path (Medium)
- Decode String (Medium)
- Maximum Frequency Stack (Hard)
- Largest Rectangle in Histogram (Hard)

### Binary Search (14 problems)
- Binary Search (Easy)
- Search Insert Position (Easy)
- Guess Number Higher or Lower (Easy)
- Sqrt(x) (Easy)
- Search a 2D Matrix (Medium)
- Koko Eating Bananas (Medium)
- Capacity To Ship Packages Within D Days (Medium)
- Find Minimum in Rotated Sorted Array (Medium)
- Search in Rotated Sorted Array (Medium)
- Search in Rotated Sorted Array II (Medium)
- Time Based Key-Value Store (Medium)
- Split Array Largest Sum (Hard)
- Median of Two Sorted Arrays (Hard)
- Find in Mountain Array (Hard)

### Linked List (14 problems)
- Reverse Linked List (Easy)
- Merge Two Sorted Lists (Easy)
- Linked List Cycle (Easy)
- Reorder List (Medium)
- Remove Nth Node From End of List (Medium)
- Copy List with Random Pointer (Medium)
- Add Two Numbers (Medium)
- Find the Duplicate Number (Medium)
- Reverse Linked List II (Medium)
- Design Circular Queue (Medium)
- LRU Cache (Medium)
- LFU Cache (Hard)
- Merge k Sorted Lists (Hard)
- Reverse Nodes in k-Group (Hard)

### Trees (23 problems)
- Binary Tree Inorder Traversal (Easy)
- Binary Tree Preorder Traversal (Easy)
- Binary Tree Postorder Traversal (Easy)
- Invert Binary Tree (Easy)
- Maximum Depth of Binary Tree (Easy)
- Diameter of Binary Tree (Easy)
- Balanced Binary Tree (Easy)
- Same Tree (Easy)
- Subtree of Another Tree (Easy)
- Lowest Common Ancestor of a Binary Search Tree (Medium)
- Insert into a Binary Search Tree (Medium)
- Delete Node in a BST (Medium)
- Binary Tree Level Order Traversal (Medium)
- Binary Tree Right Side View (Medium)
- Construct Quad Tree (Medium)
- Count Good Nodes in Binary Tree (Medium)
- Validate Binary Search Tree (Medium)
- Kth Smallest Element in a BST (Medium)
- Construct Binary Tree from Preorder and Inorder Traversal (Medium)
- House Robber III (Medium)
- Delete Leaves With a Given Value (Medium)
- Binary Tree Maximum Path Sum (Hard)
- Serialize and Deserialize Binary Tree (Hard)

### Heap / Priority Queue (12 problems)
- Kth Largest Element in a Stream (Easy)
- Last Stone Weight (Easy)
- K Closest Points to Origin (Medium)
- Kth Largest Element in an Array (Medium)
- Task Scheduler (Medium)
- Design Twitter (Medium)
- Single-Threaded CPU (Medium)
- Reorganize String (Medium)
- Longest Happy String (Medium)
- Car Pooling (Medium)
- Find Median from Data Stream (Hard)
- IPO (Hard)

### Backtracking (16 problems)
- Sum of All Subset XOR Totals (Easy)
- Subsets (Medium)
- Combination Sum (Medium)
- Combination Sum II (Medium)
- Combinations (Medium)
- Permutations (Medium)
- Subsets II (Medium)
- Permutations II (Medium)
- Word Search (Medium)
- Palindrome Partitioning (Medium)
- Letter Combinations of a Phone Number (Medium)
- Matchsticks to Square (Medium)
- Partition to K Equal Sum Subsets (Medium)
- N-Queens (Hard)
- N-Queens II (Hard)
- Word Break II (Hard)

### Tries (4 problems)
- Implement Trie (Prefix Tree) (Medium)
- Design Add and Search Words Data Structure (Medium)
- Extra Characters in a String (Medium)
- Word Search II (Hard)

### Graphs (21 problems)
- Island Perimeter (Easy)
- Verifying an Alien Dictionary (Easy)
- Find the Town Judge (Easy)
- Number of Islands (Medium)
- Max Area of Island (Medium)
- Clone Graph (Medium)
- Walls and Gates (Medium)
- Rotting Oranges (Medium)
- Pacific Atlantic Water Flow (Medium)
- Surrounded Regions (Medium)
- Open the Lock (Medium)
- Course Schedule (Medium)
- Course Schedule II (Medium)
- Graph Valid Tree (Medium)
- Course Schedule IV (Medium)
- Number of Connected Components in an Undirected Graph (Medium)
- Redundant Connection (Medium)
- Accounts Merge (Medium)
- Evaluate Division (Medium)
- Minimum Height Trees (Medium)
- Word Ladder (Hard)

### Advanced Graphs (10 problems)
- Path With Minimum Effort (Medium)
- Network Delay Time (Medium)
- Reconstruct Itinerary (Hard)
- Min Cost to Connect All Points (Medium)
- Swim in Rising Water (Hard)
- Alien Dictionary (Hard)
- Cheapest Flights Within K Stops (Medium)
- Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree (Hard)
- Build a Matrix With Conditions (Hard)
- Greatest Common Divisor Traversal (Hard)

### 1-D Dynamic Programming (17 problems)
- Climbing Stairs (Easy)
- Min Cost Climbing Stairs (Easy)
- N-th Tribonacci Number (Easy)
- House Robber (Medium)
- House Robber II (Medium)
- Longest Palindromic Substring (Medium)
- Palindromic Substrings (Medium)
- Decode Ways (Medium)
- Coin Change (Medium)
- Maximum Product Subarray (Medium)
- Word Break (Medium)
- Longest Increasing Subsequence (Medium)
- Partition Equal Subset Sum (Medium)
- Combination Sum IV (Medium)
- Perfect Squares (Medium)
- Integer Break (Medium)
- Stone Game III (Hard)

### 2-D Dynamic Programming (16 problems)
- Unique Paths (Medium)
- Unique Paths II (Medium)
- Minimum Path Sum (Medium)
- Longest Common Subsequence (Medium)
- Last Stone Weight II (Medium)
- Best Time to Buy and Sell Stock with Cooldown (Medium)
- Coin Change II (Medium)
- Target Sum (Medium)
- Interleaving String (Medium)
- Stone Game (Medium)
- Stone Game II (Medium)
- Longest Increasing Path in a Matrix (Hard)
- Distinct Subsequences (Hard)
- Edit Distance (Medium)
- Burst Balloons (Hard)
- Regular Expression Matching (Hard)

### Greedy (14 problems)
- Lemonade Change (Easy)
- Maximum Subarray (Medium)
- Maximum Sum Circular Subarray (Medium)
- Longest Turbulent Subarray (Medium)
- Jump Game (Medium)
- Jump Game II (Medium)
- Jump Game VII (Medium)
- Gas Station (Medium)
- Hand of Straights (Medium)
- Dota2 Senate (Medium)
- Merge Triplets to Form Target Triplet (Medium)
- Partition Labels (Medium)
- Valid Parenthesis String (Medium)
- Candy (Hard)

### Intervals (7 problems)
- Insert Interval (Medium)
- Merge Intervals (Medium)
- Non-overlapping Intervals (Medium)
- Meeting Rooms (Easy)
- Meeting Rooms II (Medium)
- Meeting Rooms III (Hard)
- Minimum Interval to Include Each Query (Hard)

### Math & Geometry (13 problems)
- Excel Sheet Column Title (Easy)
- Greatest Common Divisor of Strings (Easy)
- Insert Greatest Common Divisors in Linked List (Medium)
- Transpose Matrix (Easy)
- Rotate Image (Medium)
- Spiral Matrix (Medium)
- Set Matrix Zeroes (Medium)
- Happy Number (Easy)
- Plus One (Easy)
- Roman to Integer (Easy)
- Pow(x, n) (Medium)
- Multiply Strings (Medium)
- Detect Squares (Medium)

### Bit Manipulation (10 problems)
- Single Number (Easy)
- Number of 1 Bits (Easy)
- Counting Bits (Easy)
- Add Binary (Easy)
- Reverse Bits (Easy)
- Missing Number (Easy)
- Sum of Two Integers (Medium)
- Reverse Integer (Medium)
- Bitwise AND of Numbers Range (Medium)
- Minimum Array End (Medium)

## 🔗 Resources

- [NeetCode 250](https://neetcode.io/practice/practice/neetcode250) - Category roadmap and video explanations
- [LeetCode](https://leetcode.com/)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
