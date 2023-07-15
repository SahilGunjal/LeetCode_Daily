"""
leetcode: Maximum_Number_of_Events_That_Can Be Attended II

Intuition: This is leetcode hard problem and obviously noy easy. Take or not take approach is
used from recursion along with binary search tree in order to optimize it. 
"""
class Solution:
    def maxEventsValue(self, sortedEvents, total_events, i, k, memo):
        if i == total_events:
            return 0
        if k == 0:
            return 0

        if (i, k) in memo:
            return memo[(i, k)]

        ans = self.maxEventsValue(sortedEvents, total_events, i + 1, k, memo)

        next_index = bisect_left(sortedEvents, [sortedEvents[i][1] + 1])

        ans = max(ans, sortedEvents[i][2] + self.maxEventsValue(sortedEvents, total_events, next_index, k - 1, memo))

        memo[(i, k)] = ans

        return ans

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        total_events = len(events)
        memo = dict()
        return self.maxEventsValue(events, total_events, 0, k, memo)

