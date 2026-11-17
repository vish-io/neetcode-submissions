class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def sift_down(heap_size:int,root:int) -> None:
            while True:
                largest = root
                left = 2 * root + 1
                right = 2 * root + 2
                if left < heap_size and nums[left]>nums[largest]:
                    largest = left
                if right < heap_size and nums[right]>nums[largest]:
                    largest = right
                if largest == root:
                    break
                nums[root], nums[largest]= nums[largest], nums[root]
                root = largest
        for i in range(n//2-1,-1,-1):
            sift_down(n,i)
        for end in range(n-1,0,-1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(end,0)
        return nums