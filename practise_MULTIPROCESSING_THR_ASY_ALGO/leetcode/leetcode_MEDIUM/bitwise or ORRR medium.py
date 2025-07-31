class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int
        """
        n = len(nums)
        ans = [1] * n
        last = [-1] * 31
        for i in range(n - 1, -1, -1):
            for b in range(31):
                if nums[i] & (1 << b):
                    last[b] = i
            m_i = i
            for b in range(31):
                if last[b] >= 0:
                    m_i = max(m_i, last[b])
                ans[i] = m_i - i + 1

        return ans
