class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = str(x)
        if len(num) == 1:
            return int(x)
        reversed_num = num[::-1]
        if reversed_num[0] == '0':
            reversed_num = reversed_num[1:]

        if reversed_num[-1] == '-':
            reversed_num = reversed_num[:-1]
            reversed_num = '-' + reversed_num

        result = int(reversed_num)
        if result > 2147483647 or result < -2147483647:
            return 0
        return result

