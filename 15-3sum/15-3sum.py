class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        if len(nums) <= 2 : res = []
        else: nums.sort()

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                n_sum = nums[i] + nums[left] + nums[right]
                if n_sum == 0:
                    if [nums[i], nums[left], nums[right]] not in res : 
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif n_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res