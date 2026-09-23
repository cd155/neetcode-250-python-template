"""
Tests for LeetCode 71: Simplify Path
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("simplify_path", src_path / "stack" / "simplify_path.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSimplifyPath:
    """Test cases for Simplify Path problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.simplifyPath("/home/") == "/home"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.simplifyPath("/home//foo/") == "/home/foo"

    def test_example_3(self):
        """Test case from example 3"""
        result = self.solution.simplifyPath("/home/user/Documents/../Pictures")
        assert result == "/home/user/Pictures"

    def test_example_4(self):
        """Test case from example 4"""
        assert self.solution.simplifyPath("/../") == "/"

    def test_example_5(self):
        """Test case from example 5"""
        assert self.solution.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
