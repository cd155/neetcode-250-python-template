"""
Tests for LeetCode 846: Hand of Straights
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("hand_of_straights", src_path / "greedy" / "hand_of_straights.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestHandOfStraights:
    """Test cases for Hand of Straights problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.isNStraightHand([1, 2, 3, 4, 5], 4) is False
