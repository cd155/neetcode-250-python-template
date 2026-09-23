"""
Tests for LeetCode 47: Permutations II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("permutations_ii", src_path / "backtracking" / "permutations_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPermutationsII:
    """Test cases for Permutations II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert sorted(self.solution.permuteUnique([1, 1, 2])) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.permuteUnique([1, 2, 3])
        assert sorted(result) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
