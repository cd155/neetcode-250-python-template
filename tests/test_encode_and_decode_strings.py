"""
Tests for LeetCode 271: Encode and Decode Strings
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("encode_and_decode_strings", src_path / "arrays_and_hashing" / "encode_and_decode_strings.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Codec = module.Codec


class TestEncodeAndDecodeStrings:
    """Test cases for Encode and Decode Strings problem"""

    def test_example_1(self):
        """Test case from example 1"""
        codec = Codec()
        strs = ["Hello", "World"]
        encoded = codec.encode(strs)
        assert isinstance(encoded, str)
        assert codec.decode(encoded) == strs

    def test_example_2(self):
        """Test case from example 2"""
        codec = Codec()
        encoded = codec.encode([""])
        assert isinstance(encoded, str)
        assert codec.decode(encoded) == [""]

    def test_special_characters(self):
        """Strings may contain any of the 256 valid ASCII characters"""
        codec = Codec()
        strs = ["4#ab", "", "#", "a,b;c", "line\nbreak"]
        assert codec.decode(codec.encode(strs)) == strs
