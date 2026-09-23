"""
Tests for LeetCode 2709: Greatest Common Divisor Traversal
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("greatest_common_divisor_traversal", src_path / "advanced_graphs" / "greatest_common_divisor_traversal.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestGreatestCommonDivisorTraversal:
    """Test cases for Greatest Common Divisor Traversal problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canTraverseAllPairs([2, 3, 6]) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canTraverseAllPairs([3, 9, 5]) is False

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.canTraverseAllPairs([4, 3, 12, 8]) is True
