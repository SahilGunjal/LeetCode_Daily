"""
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Time Complexity = O(n)
Space Complexity = O(1)

Intuition: Create 2 ptrs and add the nodes which are less than to one node and greater than to other nodes.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessThan = ListNode(0)
        greaterThan = ListNode(0)

        lptr = lessThan
        gptr = greaterThan

        temp = head

        while temp:
            if temp.val < x:
                lptr.next = temp
                lptr = lptr.next

            else:
                gptr.next = temp
                gptr = gptr.next

            temp = temp.next

        gptr.next = None
        lptr.next = greaterThan.next

        return lessThan.next