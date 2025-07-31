class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        nums_set = set(nums)
        count = 0
        for num in nums_set:
            if num - diff in nums_set and num + diff in nums_set:
                count += 1

        return count

