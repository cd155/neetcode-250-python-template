"""
Tests for LeetCode 1011: Capacity To Ship Packages Within D Days
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("capacity_to_ship_packages_within_d_days", src_path / "binary_search" / "capacity_to_ship_packages_within_d_days.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCapacityToShipPackagesWithinDDays:
    """Test cases for Capacity To Ship Packages Within D Days problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
