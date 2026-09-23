"""
Tests for LeetCode 46: Permutations
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("permutations", src_path / "backtracking" / "permutations.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPermutations:
    """Test cases for Permutations problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.permute([1, 2, 3])
        assert sorted(result) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.permute([0, 1])) == [[0, 1], [1, 0]]

    def test_example_3(self):
        """Test case from example 3"""
        assert sorted(self.solution.permute([1])) == [[1]]
