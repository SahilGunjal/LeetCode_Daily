"""
808. Soup Servings
There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of
operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four
operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation,
we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same
time. Answers within 10-5 of the actual answer will be accepted.

Intuition: As the value of N increases, the winning rate of A approaches 1,therefore, you need to find the critical
point, which can significantly increase the execution speed. So, 4450
# How to know 4450 ? ⇣⇣⇣

        # print(dfs(1000,1000))            # 0.9765650521094358
        # print(dfs(10000,10000))          # 0.9999999999159161
        # for i in range(1000,10000):
        #     if 1-self.calculateProbability(i,i) <= 10**(-5):
        #         print(i)                 # 4451
        #         break
"""


class Solution:
    def calculateProbability(self, a, b, dp):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1

        if b <= 0:
            return 0

        if (a, b) in dp:
            return dp[(a, b)]

        ans = 0

        ans += self.calculateProbability(a - 100, b, dp)
        ans += self.calculateProbability(a - 75, b - 25, dp)
        ans += self.calculateProbability(a - 50, b - 50, dp)
        ans += self.calculateProbability(a - 25, b - 75, dp)

        dp[(a, b)] = ans / 4

        return dp[(a, b)]

    def soupServings(self, n: int) -> float:

        dp = dict()
        return 1 if n > 4450 else self.calculateProbability(n, n, dp)
