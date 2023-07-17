"""
Leetcode: 445
Add two numbers II
"""
# Approach 1 : By reversing the linked list
# time complexity : O(4n) and O(n) Space complexity


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, l):
        curr = l
        prev = None
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node

        return prev

    def add_nodes(self, ans_ptr, temp, carry):
        while temp:
            temp_sum = temp.val + carry

            if temp_sum >= 10:
                node_val = temp_sum % 10
                carry = 1
            else:
                carry = 0
                node_val = temp_sum

            if ans_ptr is None:
                ans_ptr = ListNode(node_val)
                ans_head = ans_ptr
            else:
                ans_ptr.next = ListNode(node_val)
                ans_ptr = ans_ptr.next

            temp = temp.next

        return carry, temp, ans_ptr

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_rev = self.reverseList(l1)
        l2_rev = self.reverseList(l2)

        temp1 = l1_rev
        temp2 = l2_rev
        ans_ptr = None
        ans_head = None
        carry = 0
        node_val = 0

        while temp1 and temp2:
            temp_sum = temp1.val + temp2.val + carry
            if temp_sum >= 10:
                node_val = temp_sum % 10
                carry = 1
            else:
                carry = 0
                node_val = temp_sum

            if ans_ptr is None:
                ans_ptr = ListNode(node_val)
                ans_head = ans_ptr
            else:
                ans_ptr.next = ListNode(node_val)
                ans_ptr = ans_ptr.next

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None:
            carry, temp2, ans_ptr = self.add_nodes(ans_ptr, temp2, carry)

        elif temp2 is None:
            carry, temp1, ans_ptr = self.add_nodes(ans_ptr, temp1, carry)

        if temp1 is None and temp2 is None:
            if carry != 0:
                temp_node = ListNode(carry)
                ans_ptr.next = temp_node
                ans_ptr = ans_ptr.next


        ans_node = self.reverseList(ans_head)

        return ans_node


# Another Approach is using 2 stacks
# Time complexity : ~ O(2n) = putting in stack + O(2n) = poping and adding ; n is size of linked list
# space Complexity - O(3n) : 2n for stack and n - new list

