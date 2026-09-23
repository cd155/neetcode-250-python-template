"""
Tests for LeetCode 1095: Find in Mountain Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_in_mountain_array", src_path / "binary_search" / "find_in_mountain_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
MountainArray = module.MountainArray


class TestFindInMountainArray:
    """Test cases for Find in Mountain Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        mountain_arr = MountainArray([1, 2, 3, 4, 5, 3, 1])
        assert self.solution.findInMountainArray(3, mountain_arr) == 2

    def test_example_2(self):
        """Test case from example 2"""
        mountain_arr = MountainArray([0, 1, 2, 4, 2, 1])
        assert self.solution.findInMountainArray(3, mountain_arr) == -1
