"""
Tests for LeetCode 981: Time Based Key-Value Store
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("time_based_key_value_store", src_path / "binary_search" / "time_based_key_value_store.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TimeMap = module.TimeMap


class TestTimeBasedKeyValueStore:
    """Test cases for Time Based Key-Value Store problem"""

    def test_example_1(self):
        """Test case from example 1"""
        timeMap = TimeMap()
        timeMap.set("foo", "bar", 1)
        assert timeMap.get("foo", 1) == "bar"
        assert timeMap.get("foo", 3) == "bar"
        timeMap.set("foo", "bar2", 4)
        assert timeMap.get("foo", 4) == "bar2"
        assert timeMap.get("foo", 5) == "bar2"
