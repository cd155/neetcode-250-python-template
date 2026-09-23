"""
Tests for LeetCode 202: Happy Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("happy_number", src_path / "math_and_geometry" / "happy_number.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestHappyNumber:
    """Test cases for Happy Number problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.isHappy(19) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.isHappy(2) is False
