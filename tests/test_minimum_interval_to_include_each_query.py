"""
Tests for LeetCode 1851: Minimum Interval to Include Each Query
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("minimum_interval_to_include_each_query", src_path / "intervals" / "minimum_interval_to_include_each_query.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMinimumIntervalToIncludeEachQuery:
    """Test cases for Minimum Interval to Include Each Query problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5])
        assert result == [3, 3, 1, 4]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22])
        assert result == [2, -1, 4, 6]
