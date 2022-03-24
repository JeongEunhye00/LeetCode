class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.pop(nums.index(val))
            else:
                break
        return len(nums)