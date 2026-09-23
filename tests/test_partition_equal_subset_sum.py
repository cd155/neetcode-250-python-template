"""
Tests for LeetCode 416: Partition Equal Subset Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("partition_equal_subset_sum", src_path / "dp_1d" / "partition_equal_subset_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPartitionEqualSubsetSum:
    """Test cases for Partition Equal Subset Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canPartition([1, 5, 11, 5]) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canPartition([1, 2, 3, 5]) is False
