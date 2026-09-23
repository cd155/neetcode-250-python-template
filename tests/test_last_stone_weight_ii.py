"""
Tests for LeetCode 1049: Last Stone Weight II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("last_stone_weight_ii", src_path / "dp_2d" / "last_stone_weight_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLastStoneWeightII:
    """Test cases for Last Stone Weight II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.lastStoneWeightII([31, 26, 33, 21, 40]) == 5
