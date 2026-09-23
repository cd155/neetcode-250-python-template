"""
Tests for LeetCode 410: Split Array Largest Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("split_array_largest_sum", src_path / "binary_search" / "split_array_largest_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSplitArrayLargestSum:
    """Test cases for Split Array Largest Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.splitArray([7, 2, 5, 10, 8], 2) == 18

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.splitArray([1, 2, 3, 4, 5], 2) == 9
