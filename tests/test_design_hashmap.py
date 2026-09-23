"""
Tests for LeetCode 706: Design HashMap
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("design_hashmap", src_path / "arrays_and_hashing" / "design_hashmap.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MyHashMap = module.MyHashMap


class TestDesignHashmap:
    """Test cases for Design HashMap problem"""

    def test_example_1(self):
        """Test case from example 1"""
        myHashMap = MyHashMap()
        myHashMap.put(1, 1)
        myHashMap.put(2, 2)
        assert myHashMap.get(1) == 1
        assert myHashMap.get(3) == -1
        myHashMap.put(2, 1)
        assert myHashMap.get(2) == 1
        myHashMap.remove(2)
        assert myHashMap.get(2) == -1
