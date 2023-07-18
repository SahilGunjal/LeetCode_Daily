"""
Leetcode_146 :  Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Approach: We can use orderedDict but from python 3.7 dict is ordered. So no need of orderedDict.
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.mydict = dict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.mydict:
            return -1

        val = self.mydict.pop(key)
        self.mydict[key] = val

        return val

    def put(self, key: int, value: int) -> None:
        if self.size > 0:
            if key in self.mydict:
                self.mydict.pop(key)
                self.mydict[key] = value
            else:
                self.mydict[key] = value
                self.size -= 1

        else:
            if key in self.mydict:
                self.mydict.pop(key)
                self.mydict[key] = value
            else:
                del self.mydict[next(iter(self.mydict))]
                self.mydict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Another approach is with linkedList + dictionary
