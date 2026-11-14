class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = sorted(nums)
        return x[len(x)//2]