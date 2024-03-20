"""
1669. Merge In Between Linked Lists
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
"""

# Intuition: we can get the end node of the list2 because we want to append remaining portion of list1 to it.
# Also we can get the previous element and next element of list1 before a and after b so that we can append it.
# Only tricky part here is we what if a == 0 then we have to think carefully as if we want to delete from first then
# we have to handle it by directly appending last_node to the next of b.

# Time complexity : O(n) and Space Complexity : O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        def get_last_node(list2):
            temp_head = list2
            while temp_head.next != None:
                temp_head = temp_head.next

            last_node = temp_head
            return last_node

        def get_previous_heads(list1):
            index = 0
            temp = list1
            previous_one = None
            previous_two = None
            while index <= b:
                if index + 1 == a:
                    previous_one = temp

                temp = temp.next
                index += 1

            previous_two = temp

            return previous_one, previous_two

        previous_one, previous_two = get_previous_heads(list1)
        last_node = get_last_node(list2)

        if previous_one is None:
            last_node.next = previous_two
            return list2

        else:
            previous_one.next = list2
            last_node.next = previous_two

            return list1
