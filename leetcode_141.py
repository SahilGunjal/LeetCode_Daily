"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Tc: O(n)
Sc: O(n)

Intuition: We are storing visited nodes in a set and checking while traversing that whether that node is in our
set or not if yes then return True and after all traversal return False (cycle not found).
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_list = set()

        ptr = head
        while ptr:
            if ptr in node_list:
                return True
            else:
                node_list.add(ptr)

            ptr = ptr.next

        return False


"""
Previous approach is good but it's taking extra space. Can we omit it? ...Yes
Tc:O(n)
Sc:O(1)
Intuition: We can use 2 ptrs to do this, using Floyd's Cycle-Finding Algorithm : We move firstptr one step and second
ptr 2 step if fastptr catches slow then we detect a cycle else no cycle. Here we are not using any extra space. 
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_list = set()
        ptr1 = head
        ptr2 = head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

            if ptr1 == ptr2:
                return True

        return False


