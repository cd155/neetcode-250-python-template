"""
Tests for LeetCode 739: Daily Temperatures
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("daily_temperatures", src_path / "stack" / "daily_temperatures.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestDailyTemperatures:
    """Test cases for Daily Temperatures problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
        assert result == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
