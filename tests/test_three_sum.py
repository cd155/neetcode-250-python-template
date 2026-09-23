"""
Tests for LeetCode 15: 3Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("three_sum", src_path / "two_pointers" / "three_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestThreeSum:
    """Test cases for 3Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.threeSum([-1, 0, 1, 2, -1, -4])
        assert sorted(sorted(x) for x in result) == [[-1, -1, 2], [-1, 0, 1]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(sorted(x) for x in self.solution.threeSum([0, 1, 1])) == []

    def test_example_3(self):
        """Test case from example 3"""
        assert sorted(sorted(x) for x in self.solution.threeSum([0, 0, 0])) == [[0, 0, 0]]
