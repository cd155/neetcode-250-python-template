"""
Tests for LeetCode 860: Lemonade Change
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("lemonade_change", src_path / "greedy" / "lemonade_change.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLemonadeChange:
    """Test cases for Lemonade Change problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.lemonadeChange([5, 5, 5, 10, 20]) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.lemonadeChange([5, 5, 10, 10, 20]) is False
