"""
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""

# Intuition - We know we want increasing sequence of digits from low to high lets say 4 and 5 ____ and  _____ then
# we can try putting 1,2,3...9 for the first place and then create a number. but the thing is that if you put 7 at
# beginning of the 4 digit number then end will be 10 so handle this case and generate all numbers for those digits
# then once who fall in the range of high and low will go in our ans

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        low_digits = len(str(low))
        high_digits = len(str(high))

        for digits in range(low_digits, high_digits + 1):
            for start in range(1, 9):
                if start + digits > 10:
                    break

                new_number = start
                for i in range(digits - 1):
                    new_number = new_number * 10 + (start + i + 1)

                if new_number <= high and new_number >= low:
                    ans.append(new_number)

        return ans












