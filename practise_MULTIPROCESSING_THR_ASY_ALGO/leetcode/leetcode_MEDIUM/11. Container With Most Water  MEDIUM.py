from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        s, f = 0, n - 1
        max_area = -1
        while s < f:
            if height[s] <= height[f]:
                s += 1
            else:
                f -= 1
            area = min(height[s], height[f]) * (f - s)
            if area >= max_area:
                max_area = area

        return max_area


if __name__ == '__main__':
    t = Solution()
    candidates = [1,8,6,2,5,4,8,3,7]
    t.maxArea(candidates)