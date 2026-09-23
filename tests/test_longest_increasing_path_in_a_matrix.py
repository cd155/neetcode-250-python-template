"""
Tests for LeetCode 329: Longest Increasing Path in a Matrix
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("longest_increasing_path_in_a_matrix", src_path / "dp_2d" / "longest_increasing_path_in_a_matrix.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLongestIncreasingPathInAMatrix:
    """Test cases for Longest Increasing Path in a Matrix problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.longestIncreasingPath([[1]]) == 1
