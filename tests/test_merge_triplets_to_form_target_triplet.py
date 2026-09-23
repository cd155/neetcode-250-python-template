"""
Tests for LeetCode 1899: Merge Triplets to Form Target Triplet
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_triplets_to_form_target_triplet", src_path / "greedy" / "merge_triplets_to_form_target_triplet.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMergeTripletsToFormTargetTriplet:
    """Test cases for Merge Triplets to Form Target Triplet problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) is False

    def test_example_3(self):
        """Test case from example 3"""
        triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
        target = [5, 5, 5]
        result = self.solution.mergeTriplets(triplets, target)
        assert result is True
