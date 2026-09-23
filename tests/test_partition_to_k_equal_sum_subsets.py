"""
Tests for LeetCode 698: Partition to K Equal Sum Subsets
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("partition_to_k_equal_sum_subsets", src_path / "backtracking" / "partition_to_k_equal_sum_subsets.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPartitionToKEqualSumSubsets:
    """Test cases for Partition to K Equal Sum Subsets problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canPartitionKSubsets([1, 2, 3, 4], 3) is False
