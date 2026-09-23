"""
Tests for LeetCode 1462: Course Schedule IV
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("course_schedule_iv", src_path / "graphs" / "course_schedule_iv.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCourseScheduleIV:
    """Test cases for Course Schedule IV problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False]

    def test_example_3(self):
        """Test case from example 3"""
        result = self.solution.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]])
        assert result == [True, True]
