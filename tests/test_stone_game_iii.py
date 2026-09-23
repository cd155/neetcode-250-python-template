"""
Tests for LeetCode 1406: Stone Game III
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("stone_game_iii", src_path / "dp_1d" / "stone_game_iii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestStoneGameIII:
    """Test cases for Stone Game III problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.stoneGameIII([1, 2, 3, 7]) == "Bob"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.stoneGameIII([1, 2, 3, -9]) == "Alice"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.stoneGameIII([1, 2, 3, 6]) == "Tie"
