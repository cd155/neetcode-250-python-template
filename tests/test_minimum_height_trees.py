"""
Tests for LeetCode 310: Minimum Height Trees
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("minimum_height_trees", src_path / "graphs" / "minimum_height_trees.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMinimumHeightTrees:
    """Test cases for Minimum Height Trees problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert sorted(self.solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) == [1]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
        assert sorted(result) == [3, 4]
