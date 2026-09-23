"""
Tests for LeetCode 427: Construct Quad Tree
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
spec = importlib.util.spec_from_file_location("construct_quad_tree", src_path / "trees" / "construct_quad_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
Node = module.Node


def quad_tree_to_list(root):
    """
    Serialize a Quad-Tree in level order as [isLeaf, val] pairs, with None for missing children.

    Any val is accepted for internal nodes, so they are always reported as [0, 1] like the examples.
    """
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        elif node.isLeaf:
            values.append([1, int(node.val)])
            queue.extend([None, None, None, None])
        else:
            values.append([0, 1])
            queue.extend([node.topLeft, node.topRight, node.bottomLeft, node.bottomRight])
    while values and values[-1] is None:
        values.pop()
    return values


class TestConstructQuadTree:
    """Test cases for Construct Quad Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.construct([[0, 1], [1, 0]])
        assert quad_tree_to_list(result) == [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]

    def test_example_2(self):
        """Test case from example 2"""
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
        result = self.solution.construct(grid)
        expected = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
        assert quad_tree_to_list(result) == expected
