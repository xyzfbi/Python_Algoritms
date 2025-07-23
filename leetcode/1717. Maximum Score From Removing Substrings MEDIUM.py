import re


class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_sub(s, ptr, multiplier):
            stack = []
            res = 0
            for c in s:
                stack.append(c)
                if len(stack) >= 2 and stack[-2] + stack[-1] == ptr:
                    stack.pop()
                    stack.pop()
                    res += multiplier
            return res, ''.join(stack)

        if x >= y:
            count_ab, remain = remove_sub(s, "ab", x)
            count_ba, _ = remove_sub(remain, "ba", y)
            result = count_ab + count_ba
        else:
            count_ba, remain = remove_sub(s, "ba", y)
            count_ab, _ = remove_sub(remain, "ab", x)
            result = count_ab + count_ba

        return result





if __name__ == "__main__":
    test = Solution()
    print(test.maximumGain("cdbcbbaaabab", 4, 5))
