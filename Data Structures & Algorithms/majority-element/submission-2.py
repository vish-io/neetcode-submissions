class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = sorted(nums)
        return x[len(x)//2]
        '''
        candidate = None
        count = 0
        for num in nums:
            if count==0:
                candidate = num
            count += (1 if num==candidate else -1)
            boyer moore voting algo
            limit- there is never an equality in list, i.e there is always a number which counts more than any.
            takes a number and counts it.
            if second number is found it starts decreasing the count of the first number, doing so if the second number is appearing less number of times than the current one then the majority candidate remains current one else it decreases the count until zero then when count is zero it will change the majority counting candidate to new number because it has reached the count of first one so it may get more counts and we start counting

        return candidate
        '''