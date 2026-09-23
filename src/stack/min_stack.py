"""
LeetCode 155: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int value) pushes the element value onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example:
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
       [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:
    def __init__(self):
        """
        Initialize the stack.

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement initialization
        pass

    def push(self, val):
        """
        Push val onto the stack.

        Args:
            val: int - value to push

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement push
        pass

    def pop(self):
        """
        Remove the element on top of the stack.

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement pop
        pass

    def top(self):
        """
        Get the top element.

        Returns:
            int - top element

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement top
        pass

    def getMin(self):
        """
        Retrieve the minimum element in the stack.

        Returns:
            int - minimum element

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement getMin
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("getMin():", minStack.getMin())  # -3
    minStack.pop()
    print("top():", minStack.top())  # 0
    print("getMin():", minStack.getMin())  # -2
