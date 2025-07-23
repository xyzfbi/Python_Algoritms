class Solution(object):
    def myAtoi(self, s):
        temp = s.strip()

        if not temp:
            return 0

        result_num = []
        sign = 1
        if temp[0] in '-+':
            if temp[0] == '-':
                sign = -1
            temp = temp[1:]
        temp = temp.lstrip('0')

        for char in temp:
            if char.isdigit():
                result_num.append(char)
            else:
                break

        num = sign * int(''.join(result_num)) if result_num else 0
        if num > 2147483647:
            return 2147483647
        elif num < -2147483647:
            return -2147483648
        else:
            return num

solution = Solution()
solution.myAtoi(' ')
