"""
Tests for LeetCode 973: K Closest Points to Origin
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("k_closest_points_to_origin", src_path / "heap_priority_queue" / "k_closest_points_to_origin.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestKClosestPointsToOrigin:
    """Test cases for K Closest Points to Origin problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert sorted(self.solution.kClosest([[1, 3], [-2, 2]], 1)) == [[-2, 2]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
