"""
Tests for LeetCode 494: Target Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("target_sum", src_path / "dp_2d" / "target_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestTargetSum:
    """Test cases for Target Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findTargetSumWays([1], 1) == 1
