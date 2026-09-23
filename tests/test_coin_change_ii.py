"""
Tests for LeetCode 518: Coin Change II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("coin_change_ii", src_path / "dp_2d" / "coin_change_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCoinChangeII:
    """Test cases for Coin Change II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.change(5, [1, 2, 5]) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.change(3, [2]) == 0

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.change(10, [10]) == 1
