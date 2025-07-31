class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)

        return result

if __name__ == '__main__':
    s = Solution()
    tests = [1, 2, 2, 3, 4, 5]
    r =s.targetIndices(tests, 2)
    print(r)