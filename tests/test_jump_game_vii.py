"""
Tests for LeetCode 1871: Jump Game VII
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("jump_game_vii", src_path / "greedy" / "jump_game_vii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestJumpGameVII:
    """Test cases for Jump Game VII problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canReach("011010", 2, 3) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canReach("01101110", 2, 3) is False
