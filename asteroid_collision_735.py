"""
Problem: 735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Intuition: This is stack problem the only thing that is tricky here is condition.
two asteriods will collide on each other only if uppermost element in the stack is +ve and new element which we we
are going to put is -ve and we have to look till there are elements in the stack.
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final_asteroid = []

        for astro in asteroids:

            while len(final_asteroid) > 0 and final_asteroid[-1] > 0 and astro < 0:

                if abs(astro) == final_asteroid[-1]:
                    final_asteroid.pop()
                    break

                elif abs(astro) > final_asteroid[-1]:
                    final_asteroid.pop()
                    continue

                elif abs(astro) < final_asteroid[-1]:
                    break

            else:
                final_asteroid.append(astro)

        return final_asteroid
