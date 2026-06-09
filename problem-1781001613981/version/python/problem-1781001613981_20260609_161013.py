# Last updated: 6/9/2026, 4:10:13 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        reverse = 0
6        copy = x
7        while x > 0:
8            reverse = (reverse * 10)+(x%10)
9            x//=10
10        return reverse == copy