"""
Tests for LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
"""

import pytest
import sys
from collections import deque
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("lowest_common_ancestor_of_a_binary_search_tree", src_path / "trees" / "lowest_common_ancestor_of_a_binary_search_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


def build_tree(values):
    """Build a binary tree from its level-order list (None marks a missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def find_node(root, value):
    """Return the node of the BST that holds value."""
    while root and root.val != value:
        root = root.left if value < root.val else root.right
    return root


class TestLowestCommonAncestorOfABinarySearchTree:
    """Test cases for Lowest Common Ancestor of a Binary Search Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        result = self.solution.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 8))
        assert result is find_node(root, 6)

    def test_example_2(self):
        """Test case from example 2"""
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        result = self.solution.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 4))
        assert result is find_node(root, 2)

    def test_example_3(self):
        """Test case from example 3"""
        root = build_tree([2, 1])
        result = self.solution.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 1))
        assert result is find_node(root, 2)
