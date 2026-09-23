"""
Tests for LeetCode 40: Combination Sum II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("combination_sum_ii", src_path / "backtracking" / "combination_sum_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCombinationSumII:
    """Test cases for Combination Sum II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        assert sorted(sorted(x) for x in result) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.combinationSum2([2, 5, 2, 1, 2], 5)
        assert sorted(sorted(x) for x in result) == [[1, 2, 2], [5]]
