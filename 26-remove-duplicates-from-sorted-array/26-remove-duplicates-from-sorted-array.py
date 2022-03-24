class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
            
        while i != len(nums):
            if len(nums) == 1 or i == len(nums)-1:
                i = len(nums)
                break
            
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                if i+1 == len(nums)-1:
                    i += 2
                else:
                    i += 1
        return i