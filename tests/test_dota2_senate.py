"""
Tests for LeetCode 649: Dota2 Senate
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("dota2_senate", src_path / "greedy" / "dota2_senate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestDota2Senate:
    """Test cases for Dota2 Senate problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.predictPartyVictory("RD") == "Radiant"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.predictPartyVictory("RDD") == "Dire"
