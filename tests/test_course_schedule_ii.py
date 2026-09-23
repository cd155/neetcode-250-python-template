"""
Tests for LeetCode 210: Course Schedule II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("course_schedule_ii", src_path / "graphs" / "course_schedule_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def is_valid_order(num_courses, prerequisites, order):
    """Check that order takes every course once and respects every prerequisite."""
    if not isinstance(order, list) or sorted(order) != list(range(num_courses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[before] < position[course] for course, before in prerequisites)


class TestCourseScheduleII:
    """Test cases for Course Schedule II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (any valid order is accepted)"""
        result = self.solution.findOrder(2, [[1, 0]])
        assert is_valid_order(2, [[1, 0]], result)

    def test_example_2(self):
        """Test case from example 2 (any valid order is accepted)"""
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.solution.findOrder(4, prerequisites)
        assert is_valid_order(4, prerequisites, result)

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.findOrder(1, []) == [0]

    def test_impossible(self):
        """A cycle makes it impossible to finish all courses"""
        assert self.solution.findOrder(2, [[1, 0], [0, 1]]) == []
