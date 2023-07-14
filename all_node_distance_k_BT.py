"""
Problem : Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the
values of all nodes that have a distance k from the target node. You can return the answer in any order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse_tree(self, node):
        q = deque()
        parent_dict = dict()
        q.append(node)
        while q:
            current = q.pop()
            if current.left:
                parent_dict[current.left] = current
                q.append(current.left)

            if current.right:
                parent_dict[current.right] = current
                q.append(current.right)

        return parent_dict

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_dict = self.traverse_tree(root)
        que = deque()
        visited = set()
        curr_level = 0

        que.append(target)
        visited.add(target)

        while que:
            que_size = len(que)
            if curr_level == k:
                break
            curr_level += 1
            for i in range(que_size):
                curr = que.popleft()
                if curr.left and curr.left not in visited:
                    que.append(curr.left)
                    visited.add(curr.left)

                if curr.right and curr.right not in visited:
                    que.append(curr.right)
                    visited.add(curr.right)

                if curr in parent_dict:
                    if parent_dict[curr] and parent_dict[curr] not in visited:
                        que.append(parent_dict[curr])
                        visited.add(parent_dict[curr])

        ans = []
        for element in que:
            ans.append(element.val)

        return ans




