"""
Tests for LeetCode 146: LRU Cache
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("lru_cache", src_path / "linked_list" / "lru_cache.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
LRUCache = module.LRUCache


class TestLRUCache:
    """Test cases for LRU Cache problem"""

    def test_example_1(self):
        """Test case from example 1"""
        lruCache = LRUCache(2)
        lruCache.put(1, 1)
        lruCache.put(2, 2)
        assert lruCache.get(1) == 1
        lruCache.put(3, 3)
        assert lruCache.get(2) == -1
        lruCache.put(4, 4)
        assert lruCache.get(1) == -1
        assert lruCache.get(3) == 3
        assert lruCache.get(4) == 4
