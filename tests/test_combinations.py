"""
Tests for LeetCode 77: Combinations
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("combinations", src_path / "backtracking" / "combinations.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCombinations:
    """Test cases for Combinations problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.combine(4, 2)
        assert sorted(sorted(x) for x in result) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(sorted(x) for x in self.solution.combine(1, 1)) == [[1]]
