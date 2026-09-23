"""
Tests for LeetCode 399: Evaluate Division
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("evaluate_division", src_path / "graphs" / "evaluate_division.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestEvaluateDivision:
    """Test cases for Evaluate Division problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        result = self.solution.calcEquation(equations, values, queries)
        assert result == pytest.approx([6.0, 0.5, -1.0, 1.0, -1.0])

    def test_example_2(self):
        """Test case from example 2"""
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        result = self.solution.calcEquation(equations, values, queries)
        assert result == pytest.approx([3.75, 0.4, 5.0, 0.2])

    def test_example_3(self):
        """Test case from example 3"""
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        result = self.solution.calcEquation(equations, values, queries)
        assert result == pytest.approx([0.5, 2.0, -1.0, -1.0])
