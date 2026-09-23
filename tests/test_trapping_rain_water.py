"""
Tests for LeetCode 42: Trapping Rain Water
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("trapping_rain_water", src_path / "two_pointers" / "trapping_rain_water.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestTrappingRainWater:
    """Test cases for Trapping Rain Water problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.trap([4, 2, 0, 3, 2, 5]) == 9
