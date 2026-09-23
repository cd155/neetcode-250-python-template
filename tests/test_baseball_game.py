"""
Tests for LeetCode 682: Baseball Game
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("baseball_game", src_path / "stack" / "baseball_game.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestBaseballGame:
    """Test cases for Baseball Game problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.calPoints(["5", "2", "C", "D", "+"]) == 30

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.calPoints(["1", "C"]) == 0
