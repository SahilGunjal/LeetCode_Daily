"""
Leetcode: 50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Approach 1: Naive : Just loop through n times and calculate. time complexity is linear. O(n)
Ans: x**n or simple for loop.
"""

# Approach 2 : We can solve this in logarithmic time complexity.
# if n is even = (x*x)^n/2
# if n is odd = x*(x*x)^n/2
# if n is < 0 then we know n raise to -ve means 1/n raise to +ve

class Solution:
    def calculateInLog(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.calculateInLog(x, -n)

        if n % 2 == 0:
            return self.calculateInLog(x * x, n / 2)

        else:
            return x * self.calculateInLog(x * x, (n - 1) / 2)

    def myPow(self, x: float, n: int) -> float:
        return self.calculateInLog(x, n)


