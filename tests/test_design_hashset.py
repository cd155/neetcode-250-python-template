"""
Tests for LeetCode 705: Design HashSet
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("design_hashset", src_path / "arrays_and_hashing" / "design_hashset.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MyHashSet = module.MyHashSet


class TestDesignHashset:
    """Test cases for Design HashSet problem"""

    def test_example_1(self):
        """Test case from example 1"""
        myHashSet = MyHashSet()
        myHashSet.add(1)
        myHashSet.add(2)
        assert myHashSet.contains(1) is True
        assert myHashSet.contains(3) is False
        myHashSet.add(2)
        assert myHashSet.contains(2) is True
        myHashSet.remove(2)
        assert myHashSet.contains(2) is False
