class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height)-1
        L, R, res = 0, len(height)-1, 0
        for w in range(width, 0, -1):
            if height[L] <= height[R]:
                res = max(res, height[L]*w)
                L += 1
            else:
                res = max(res, height[R]*w)
                R -= 1
        return res