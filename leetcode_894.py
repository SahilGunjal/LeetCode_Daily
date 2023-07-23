"""
Leetcode 894: 894. All Possible Full Binary Trees
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer
must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.


Intuition: It is a dp problem and can be solved with recursion as well.
Approach :1. If n is even we can't make a full binary tree.
 2. first we know 3 nodes must be there if n>1. so store dp[1] and dp[3]
 3. After 3 we have to build tree with all the diff possibilities so for loop for i = 5 to i = n+1
 4. we know that nodes will be of even and after 5 it will increase by 2 so +2
 5. then try from l = 1 to l= n-1 and r = n-1 to r = 1. These will be the left and right nodes.
 6. For n = 5 there are total 2 ways so use that from dp and then loop for dp[left] and dp[right] to get all
 the combinations.
 7. Return dp[n] at the end to get all the possible trees.
 ---------This is Bottom Up Approach-----------
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        my_dict = defaultdict(list)

        if n % 2 == 0:
            return []

        my_dict[1].append(TreeNode(0))

        temp = TreeNode(0)
        temp.left = TreeNode(0)
        temp.right = TreeNode(0)
        my_dict[3].append(temp)

        for i in range(5, n + 1, 2):
            left = 1
            right = i - left - 1

            while right >= 1:
                for all_left in my_dict[left]:
                    for all_right in my_dict[right]:
                        temp = TreeNode(0)
                        temp.left = all_left
                        temp.right = all_right
                        my_dict[i].append(temp)

                right -= 2
                left += 2

        return my_dict[n]

