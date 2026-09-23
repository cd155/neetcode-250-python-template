"""
Tests for LeetCode 49: Group Anagrams
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("group_anagrams", src_path / "arrays_and_hashing" / "group_anagrams.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestGroupAnagrams:
    """Test cases for Group Anagrams problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert sorted(sorted(x) for x in result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(sorted(x) for x in self.solution.groupAnagrams([""])) == [[""]]

    def test_example_3(self):
        """Test case from example 3"""
        assert sorted(sorted(x) for x in self.solution.groupAnagrams(["a"])) == [["a"]]
