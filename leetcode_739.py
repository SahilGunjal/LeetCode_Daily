"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no
future day for which this is possible, keep answer[i] == 0 instead.

"""
# Intuition : we want next greater value -
# Brute force: O(n^2) - 2 for loops
# better option - O(n) space and time -

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    monotonic_decreasing_stack = []
    next_warmer_day_difference = [0]*len(temperatures)
    for index, temp in enumerate(temperatures):
        if len(monotonic_decreasing_stack) == 0 or temp <= monotonic_decreasing_stack[-1][0]:
            monotonic_decreasing_stack.append((temp,index))

        else:
            while monotonic_decreasing_stack and temp > monotonic_decreasing_stack[-1][0]:
                top_stack_val, top_stack_index = monotonic_decreasing_stack.pop()
                next_warmer_day_difference[top_stack_index] = index - top_stack_index

            monotonic_decreasing_stack.append((temp,index))

    return next_warmer_day_difference


# Best - Without the Stack

    n = len(temperatures)
    ans = [0] * n
    for i in range(n - 2, -1, -1):
        temp_ind = i + 1
        while temp_ind < n and temperatures[temp_ind] <= temperatures[i] and ans[temp_ind] != 0:
            temp_ind = temp_ind + ans[temp_ind]

        if temp_ind < n and temperatures[temp_ind] > temperatures[i]:
            ans[i] = temp_ind - i

    return ans