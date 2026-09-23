"""
Tests for LeetCode 168: Excel Sheet Column Title
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("excel_sheet_column_title", src_path / "math_and_geometry" / "excel_sheet_column_title.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestExcelSheetColumnTitle:
    """Test cases for Excel Sheet Column Title problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.convertToTitle(1) == "A"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.convertToTitle(28) == "AB"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.convertToTitle(701) == "ZY"
