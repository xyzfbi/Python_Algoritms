class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        freq = [0] * 100
        ans = 0
        for a, b in dominoes:
            key = a * 10 +b  if a <= b else b * 10 +a
            ans += freq[key]
            freq[key] += 1
        return ans
