"""
Tests for LeetCode 64: Minimum Path Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("minimum_path_sum", src_path / "dp_2d" / "minimum_path_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMinimumPathSum:
    """Test cases for Minimum Path Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
