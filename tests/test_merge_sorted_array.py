"""
Tests for LeetCode 88: Merge Sorted Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_sorted_array", src_path / "two_pointers" / "merge_sorted_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMergeSortedArray:
    """Test cases for Merge Sorted Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        nums1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(nums1, 3, [2, 5, 6], 3)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_example_2(self):
        """Test case from example 2"""
        nums1 = [1]
        self.solution.merge(nums1, 1, [], 0)
        assert nums1 == [1]

    def test_example_3(self):
        """Test case from example 3"""
        nums1 = [0]
        self.solution.merge(nums1, 0, [1], 1)
        assert nums1 == [1]
