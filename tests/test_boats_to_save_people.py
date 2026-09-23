"""
Tests for LeetCode 881: Boats to Save People
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("boats_to_save_people", src_path / "two_pointers" / "boats_to_save_people.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestBoatsToSavePeople:
    """Test cases for Boats to Save People problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.numRescueBoats([1, 2], 3) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.numRescueBoats([3, 2, 2, 1], 3) == 3

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.numRescueBoats([3, 5, 3, 4], 5) == 4
