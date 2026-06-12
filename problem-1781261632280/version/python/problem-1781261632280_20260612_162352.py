# Last updated: 6/12/2026, 4:23:52 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        low=0
4        high = len(nums)-1
5        while low <=high:
6            if nums[low] == val:
7                nums[low],nums[high] = nums[high], nums[low]
8                high -= 1
9            else:
10                low += 1
11        return low