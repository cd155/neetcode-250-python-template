"""
Tests for LeetCode 997: Find the Town Judge
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_the_town_judge", src_path / "graphs" / "find_the_town_judge.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindTheTownJudge:
    """Test cases for Find the Town Judge problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findJudge(2, [[1, 2]]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findJudge(3, [[1, 3], [2, 3]]) == 3

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
