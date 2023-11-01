"""
Leetcode 501.Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Naive Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        if not root:
            return ans
        my_dict = dict()

        def recursive(node):
            if node is None:
                return

            if node.val in my_dict:
                my_dict[node.val] += 1
            else:
                my_dict[node.val] = 1

            recursive(node.left)
            recursive(node.right)

        recursive(root)
        if len(my_dict) == 0:
            return my_dict.keys()

        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        i = 0
        mode_val = 0
        for key, val in sorted_dict.items():
            if i == 0:
                ans.append(key)
                mode_val = val

            else:
                if val == mode_val:
                    ans.append(key)

                else:
                    break

            i += 1

        return ans


    # Solution with better time and space complexity

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def findMode(self, root: Optional[TreeNode]) -> List[int]:
            prev_node = None
            ans = []
            if not root:
                return ans
            max_count = 0
            count = 0

            def recursive(node):
                if node is None:
                    return
                nonlocal prev_node, max_count, count

                recursive(node.left)

                if prev_node and prev_node.val == node.val:
                    count += 1

                else:
                    count = 1

                if count > max_count:
                    ans.clear()
                    max_count = count
                    ans.append(node.val)

                elif count == max_count:
                    ans.append(node.val)

                prev_node = node

                recursive(node.right)

            # Do Inorder so that items will be in sorted order
            recursive(root)
            return ans

