"""
Tests for LeetCode 26: Remove Duplicates from Sorted Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("remove_duplicates_from_sorted_array", src_path / "two_pointers" / "remove_duplicates_from_sorted_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRemoveDuplicatesFromSortedArray:
    """Test cases for Remove Duplicates from Sorted Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        nums = [1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_example_2(self):
        """Test case from example 2"""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [0, 1, 2, 3, 4]
