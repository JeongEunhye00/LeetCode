class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums)-1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                k = i-1
                break
        if k == len(nums)-1: nums[:] = nums[::-1]
        else:
            for i in range(len(nums[k+1:]), 0, -1):
                if nums[k+i] > nums[k]:
                    tmp = nums[k]
                    nums[k] = nums[k+i]
                    nums[k+i] = tmp
                    nums[k+1:] = nums[k+1:][::-1]
                    break