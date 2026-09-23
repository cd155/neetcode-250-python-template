"""
Tests for LeetCode 90: Subsets II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("subsets_ii", src_path / "backtracking" / "subsets_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSubsetsII:
    """Test cases for Subsets II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.subsetsWithDup([1, 2, 2])
        assert sorted(sorted(x) for x in result) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(sorted(x) for x in self.solution.subsetsWithDup([0])) == [[], [0]]
