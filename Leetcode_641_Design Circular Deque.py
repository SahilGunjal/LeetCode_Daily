"""
As per the name, need to Design Circular Deque.

First thought in my mind to do this is linked list but then if it's just single then while deleting from rear we need
to traverse whole to get the element before previous. So best way to do is doubly linkedList.
"""

# Solution

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.limit = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.front == None:
            self.count = 1
            tempNode = LinkedNode(value)
            self.rear = tempNode
            self.front = tempNode
            self.rear.next = self.front
            self.front.prev = self.rear
            return True
        else:
            if self.isFull() == False:
                self.count += 1
                newNode = LinkedNode(value)
                newNode.next = self.front
                self.front.prev = newNode
                self.front = newNode
                self.rear.next = self.front
                return True
            else:
                return False

    def insertLast(self, value: int) -> bool:
        if self.rear == None:
            self.count = 1
            tempNode = LinkedNode(value)
            self.rear = tempNode
            self.front = tempNode
            self.rear.next = self.front
            self.front.prev = self.rear
            return True
        else:
            if self.isFull() == False:
                self.count += 1
                newNode = LinkedNode(value)
                self.rear.next = newNode
                newNode.prev = self.rear
                self.rear = newNode
                self.rear.next = self.front
                return True
            else:
                return False

    def deleteFront(self) -> bool:
        if self.front == None:
            return False
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.count = 0
            return True
        else:
            nextFront = self.front.next
            nextFront.prev = self.rear
            self.front = nextFront
            self.count -= 1
            return True

    def deleteLast(self) -> bool:
        if self.rear == None:
            return False
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.count = 0
            return True
        else:
            newRear = self.rear.prev
            newRear.next = self.front
            self.rear = newRear
            self.count -= 1
            return True

    def getFront(self) -> int:
        if self.front == None:
            return -1
        else:
            return self.front.val

    def getRear(self) -> int:
        if self.rear == None:
            return -1
        else:
            return self.rear.val

    def isEmpty(self) -> bool:
        return self.front == None

    def isFull(self) -> bool:
        return self.count == self.limit

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()