"""
Tests for LeetCode 778: Swim in Rising Water
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("swim_in_rising_water", src_path / "advanced_graphs" / "swim_in_rising_water.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSwimInRisingWater:
    """Test cases for Swim in Rising Water problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.swimInWater([[0, 2], [1, 3]]) == 3

    def test_example_2(self):
        """Test case from example 2"""
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        result = self.solution.swimInWater(grid)
        assert result == 16
