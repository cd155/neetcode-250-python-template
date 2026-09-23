"""
Tests for LeetCode 4: Median of Two Sorted Arrays
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("median_of_two_sorted_arrays", src_path / "binary_search" / "median_of_two_sorted_arrays.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMedianOfTwoSortedArrays:
    """Test cases for Median of Two Sorted Arrays problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findMedianSortedArrays([1, 3], [2]) == pytest.approx(2.0)

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findMedianSortedArrays([1, 2], [3, 4]) == pytest.approx(2.5)
