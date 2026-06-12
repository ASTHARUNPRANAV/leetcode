# Last updated: 6/12/2026, 4:21:11 PM
1class Solution:
2    def removeDuplicates(self, nums):
3        index = 1
4        for i in range(1, len(nums)):
5            if nums[i] != nums[i - 1]:
6                nums[index] = nums[i]
7                index += 1
8        return index