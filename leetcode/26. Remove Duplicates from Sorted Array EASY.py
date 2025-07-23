class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)

if __name__ == '__main__':
    test = Solution()
    print(test.removeDuplicates([1,1,1,2,2,3,3,4,4,5]))
