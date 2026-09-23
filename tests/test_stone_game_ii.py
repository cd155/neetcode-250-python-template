"""
Tests for LeetCode 1140: Stone Game II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("stone_game_ii", src_path / "dp_2d" / "stone_game_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestStoneGameII:
    """Test cases for Stone Game II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.stoneGameII([2, 7, 9, 4, 4]) == 10

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.stoneGameII([1, 2, 3, 4, 5, 100]) == 104
