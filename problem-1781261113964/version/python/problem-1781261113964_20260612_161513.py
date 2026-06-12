# Last updated: 6/12/2026, 4:15:13 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {'I':1, 'V':5, 'X':10, 'L':50,
4                 'C':100, 'D':500, 'M':1000}
5        
6        result = 0
7        for i in range(len(s)):
8            curr = roman[s[i]]
9            next_val = roman[s[i+1]] if i+1 < len(s) else 0
10            
11            if curr < next_val:
12                result -= curr
13            else:
14                result += curr
15        
16        return result