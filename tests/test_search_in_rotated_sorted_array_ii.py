"""
Tests for LeetCode 81: Search in Rotated Sorted Array II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("search_in_rotated_sorted_array_ii", src_path / "binary_search" / "search_in_rotated_sorted_array_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSearchInRotatedSortedArrayII:
    """Test cases for Search in Rotated Sorted Array II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.search([2, 5, 6, 0, 0, 1, 2], 0) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.search([2, 5, 6, 0, 0, 1, 2], 3) is False
