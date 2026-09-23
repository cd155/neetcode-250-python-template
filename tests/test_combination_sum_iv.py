"""
Tests for LeetCode 377: Combination Sum IV
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("combination_sum_iv", src_path / "dp_1d" / "combination_sum_iv.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCombinationSumIV:
    """Test cases for Combination Sum IV problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.combinationSum4([1, 2, 3], 4) == 7

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.combinationSum4([9], 3) == 0
