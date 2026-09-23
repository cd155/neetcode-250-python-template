"""
Tests for LeetCode 2402: Meeting Rooms III
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("meeting_rooms_iii", src_path / "intervals" / "meeting_rooms_iii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMeetingRoomsIII:
    """Test cases for Meeting Rooms III problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
