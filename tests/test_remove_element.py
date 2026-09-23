"""
Tests for LeetCode 27: Remove Element
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("remove_element", src_path / "arrays_and_hashing" / "remove_element.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRemoveElement:
    """Test cases for Remove Element problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        nums = [3, 2, 2, 3]
        k = self.solution.removeElement(nums, 3)
        assert k == 2
        assert sorted(nums[:k]) == [2, 2]

    def test_example_2(self):
        """Test case from example 2"""
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = self.solution.removeElement(nums, 2)
        assert k == 5
        assert sorted(nums[:k]) == [0, 0, 1, 3, 4]
