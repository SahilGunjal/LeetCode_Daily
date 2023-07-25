"""
852. Peak Index in a Mountain Array
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ...
> arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
"""

# Naive Approach : return arr.index(max(arr))

# My solution:(binary search)  : Faster

class Solution:
    def bSearch(self, l, r, arr):
        while r >= l:
            mid = l + (r - l) // 2

            if (r - l) == 1:
                if arr[l] < arr[r]:
                    return r
                else:
                    return l

            if (arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]):
                return mid

            elif arr[mid - 1] < arr[mid] and arr[mid + 1] > arr[mid]:
                return self.bSearch(mid + 1, r, arr)
            else:
                print(f'{l},{mid - 1}')
                return self.bSearch(l, mid - 1, arr)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        return self.bSearch(0, len(arr) - 1, arr)

# Another Solution: less code but slower

class Solution:
    def bSearch(self, l, r, arr):
        while r >= l:
            mid = l + (r - l) // 2

            if (arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]):
                return mid

            elif arr[mid + 1] > arr[mid]:
                return self.bSearch(mid + 1, r, arr)
            else:
                return self.bSearch(l, mid - 1, arr)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        return self.bSearch(0, len(arr) - 1, arr)

