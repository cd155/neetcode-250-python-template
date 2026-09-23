"""
Tests for LeetCode 18: 4Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("four_sum", src_path / "two_pointers" / "four_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFourSum:
    """Test cases for 4Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.fourSum([1, 0, -1, 0, -2, 2], 0)
        assert sorted(sorted(x) for x in result) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.fourSum([2, 2, 2, 2, 2], 8)
        assert sorted(sorted(x) for x in result) == [[2, 2, 2, 2]]
