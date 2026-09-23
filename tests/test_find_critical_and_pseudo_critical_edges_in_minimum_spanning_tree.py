"""
Tests for LeetCode 1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree", src_path / "advanced_graphs" / "find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindCriticalAndPseudoCriticalEdgesInMinimumSpanningTree:
    """Test cases for Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (indices may be in any order)"""
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
        result = self.solution.findCriticalAndPseudoCriticalEdges(5, edges)
        assert [sorted(indices) for indices in result] == [[0, 1], [2, 3, 4, 5]]

    def test_example_2(self):
        """Test case from example 2 (indices may be in any order)"""
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
        result = self.solution.findCriticalAndPseudoCriticalEdges(4, edges)
        assert [sorted(indices) for indices in result] == [[], [0, 1, 2, 3]]
