# Last updated: 6/12/2026, 4:18:13 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        mapping = {')': '(', '}': '{', ']': '['}
4        stack = []
5        for char in s:
6            if char in mapping.values():
7                stack.append(char)
8            elif char in mapping:
9                if not stack or mapping[char] != stack.pop():
10                    return False
11        return not stack
12        