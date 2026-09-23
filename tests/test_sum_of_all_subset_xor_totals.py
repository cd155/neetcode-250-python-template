"""
Tests for LeetCode 1863: Sum of All Subset XOR Totals
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("sum_of_all_subset_xor_totals", src_path / "backtracking" / "sum_of_all_subset_xor_totals.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSumOfAllSubsetXorTotals:
    """Test cases for Sum of All Subset XOR Totals problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.subsetXORSum([1, 3]) == 6

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.subsetXORSum([5, 1, 6]) == 28

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480
