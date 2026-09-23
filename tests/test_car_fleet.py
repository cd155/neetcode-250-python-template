"""
Tests for LeetCode 853: Car Fleet
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("car_fleet", src_path / "stack" / "car_fleet.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCarFleet:
    """Test cases for Car Fleet problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.carFleet(10, [3], [3]) == 1

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
