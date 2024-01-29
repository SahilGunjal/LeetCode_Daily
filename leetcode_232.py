"""
232. Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the
functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is
empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque
(double-ended queue) as long as you use only a stack's standard operations.
"""

# Intuition: While push add everything in the first. If want to pop...first push everything except the first element in
# the second stack and then save the value of first in variable and then pop it and then again put everything from the
# second stack to first. And for peak as its just list use [0].

# Time complexity: Push -O(1) Pop()-O(2*n) ..(worst) and peek() - O(1)

class MyQueue:

    def __init__(self):
        self.first_stack = deque()
        self.second_stack = deque()

    def push(self, x: int) -> None:
        self.first_stack.append(x)

    def pop(self) -> int:
        if len(self.first_stack) == 1:
            return self.first_stack.pop()
        else:
            val = None
            while len(self.first_stack) != 1:
                self.second_stack.append(self.first_stack.pop())

            val = self.first_stack.pop()

            while self.second_stack:
                self.first_stack.append(self.second_stack.pop())

            return val

    def peek(self) -> int:
        return self.first_stack[0]

    def empty(self) -> bool:
        return len(self.first_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()