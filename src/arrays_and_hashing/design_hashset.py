"""
LeetCode 705: Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the
  HashSet, do nothing.

Example:
Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
       [[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output: [null, null, null, true, false, null, true, null, false]
Explanation:
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:
- 0 <= key <= 10^6
- At most 10^4 calls will be made to add, remove, and contains.
"""


class MyHashSet:
    def __init__(self):
        """
        Initialize the hash set.

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement initialization
        pass

    def add(self, key):
        """
        Insert key into the set.

        Args:
            key: int - key

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement add
        pass

    def remove(self, key):
        """
        Remove key from the set if present.

        Args:
            key: int - key

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement remove
        pass

    def contains(self, key):
        """
        Check whether key exists in the set.

        Args:
            key: int - key

        Returns:
            bool - True if key is in the set

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement contains
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    print("contains(1):", myHashSet.contains(1))  # True
    print("contains(3):", myHashSet.contains(3))  # False
    myHashSet.add(2)
    print("contains(2):", myHashSet.contains(2))  # True
    myHashSet.remove(2)
    print("contains(2):", myHashSet.contains(2))  # False
