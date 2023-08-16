"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
 array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Naive Approach : go through 3 k times find max and add it to ans
tc: o(n*k)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        que = deque()
        for i in range(n - k + 1):
            max = float('-inf')
            for j in range(i, i + k):
                if nums[j] > max:
                    max = nums[j]

            que.append(max)

        ans = []
        while que:
            ans.append(que.popleft())

        return ans




"""
O(n) approach : Using queue

intuition: we have to add the elements in decreasing order remove the elements which are beyond the range of current 
window and we dont want elements which are less than current element so remove it also and add the current element to the
que and add front element of que to the ans array. 
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        que = deque()

        for i in range(len(nums)):
            if que and que[0] == i - k:
                que.popleft()

            while que and nums[que[-1]] < nums[i]:
                que.pop()

            que.append(i)
            # print(que)
            if i >= k - 1:
                ans.append(nums[que[0]])
                # print(ans)

        return ans
