"""
Tests for LeetCode 912: Sort an Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("sort_an_array", src_path / "arrays_and_hashing" / "sort_an_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSortAnArray:
    """Test cases for Sort an Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
