"""
Tests for LeetCode 374: Guess Number Higher or Lower
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("guess_number_higher_or_lower", src_path / "binary_search" / "guess_number_higher_or_lower.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestGuessNumberHigherOrLower:
    """Test cases for Guess Number Higher or Lower problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        module.pick = 6
        assert self.solution.guessNumber(10) == 6

    def test_example_2(self):
        """Test case from example 2"""
        module.pick = 1
        assert self.solution.guessNumber(1) == 1

    def test_example_3(self):
        """Test case from example 3"""
        module.pick = 1
        assert self.solution.guessNumber(2) == 1
