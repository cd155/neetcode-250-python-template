"""
LeetCode 622: Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data
structure in which the operations are performed based on FIFO (First In First Out)
principle, and the last position is connected back to the first position to make a
circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front
of the queue. In a normal queue, once the queue becomes full, we cannot insert the next
element even if there is a space in front of the queue. But using the circular queue, we
can use the space to store new values.

Implement the MyCircularQueue class:

- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If the queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true if
  the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the
  operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your
programming language.

Example:
Input: ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
       [[3], [1], [2], [3], [4], [], [], [], [4], []]
Output: [null, true, true, true, false, 3, true, true, true, 4]
Explanation:
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""


class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize the queue with size k.

        Args:
            k: int - capacity of the queue

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement initialization
        pass

    def enQueue(self, value):
        """
        Insert an element into the queue.

        Args:
            value: int - value to insert

        Returns:
            bool - True if the operation succeeds

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement enQueue
        pass

    def deQueue(self):
        """
        Delete an element from the queue.

        Returns:
            bool - True if the operation succeeds

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement deQueue
        pass

    def Front(self):
        """
        Get the front item.

        Returns:
            int - front item, or -1 if empty

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement Front
        pass

    def Rear(self):
        """
        Get the last item.

        Returns:
            int - last item, or -1 if empty

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement Rear
        pass

    def isEmpty(self):
        """
        Check whether the queue is empty.

        Returns:
            bool - True if empty

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement isEmpty
        pass

    def isFull(self):
        """
        Check whether the queue is full.

        Returns:
            bool - True if full

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement isFull
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    print("enQueue(1):", myCircularQueue.enQueue(1))  # True
    print("enQueue(2):", myCircularQueue.enQueue(2))  # True
    print("enQueue(3):", myCircularQueue.enQueue(3))  # True
    print("enQueue(4):", myCircularQueue.enQueue(4))  # False
    print("Rear():", myCircularQueue.Rear())  # 3
    print("isFull():", myCircularQueue.isFull())  # True
    print("deQueue():", myCircularQueue.deQueue())  # True
    print("enQueue(4):", myCircularQueue.enQueue(4))  # True
    print("Rear():", myCircularQueue.Rear())  # 4
