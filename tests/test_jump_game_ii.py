"""
Tests for LeetCode 45: Jump Game II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("jump_game_ii", src_path / "greedy" / "jump_game_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestJumpGameII:
    """Test cases for Jump Game II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.jump([2, 3, 1, 1, 4]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.jump([2, 3, 0, 1, 4]) == 2
