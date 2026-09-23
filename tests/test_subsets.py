"""
Tests for LeetCode 78: Subsets
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("subsets", src_path / "backtracking" / "subsets.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSubsets:
    """Test cases for Subsets problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.subsets([1, 2, 3])
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        assert sorted(sorted(x) for x in result) == expected

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(sorted(x) for x in self.solution.subsets([0])) == [[], [0]]
