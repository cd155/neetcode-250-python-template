"""
Tests for LeetCode 460: LFU Cache
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("lfu_cache", src_path / "linked_list" / "lfu_cache.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
LFUCache = module.LFUCache


class TestLFUCache:
    """Test cases for LFU Cache problem"""

    def test_example_1(self):
        """Test case from example 1"""
        lfuCache = LFUCache(2)
        lfuCache.put(1, 1)
        lfuCache.put(2, 2)
        assert lfuCache.get(1) == 1
        lfuCache.put(3, 3)
        assert lfuCache.get(2) == -1
        assert lfuCache.get(3) == 3
        lfuCache.put(4, 4)
        assert lfuCache.get(1) == -1
        assert lfuCache.get(3) == 3
        assert lfuCache.get(4) == 4
