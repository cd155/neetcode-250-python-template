"""
Tests for LeetCode 39: Combination Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("combination_sum", src_path / "backtracking" / "combination_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCombinationSum:
    """Test cases for Combination Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.combinationSum([2, 3, 6, 7], 7)
        assert sorted(sorted(x) for x in result) == [[2, 2, 3], [7]]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.combinationSum([2, 3, 5], 8)
        assert sorted(sorted(x) for x in result) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    def test_example_3(self):
        """Test case from example 3"""
        assert sorted(sorted(x) for x in self.solution.combinationSum([2], 1)) == []
