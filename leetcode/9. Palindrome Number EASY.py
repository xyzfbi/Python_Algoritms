"""
Given an integer x, return true if x is a

, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x % 10 == 0 and x != 0:
            return False
        reversed_half = 0  # for optimization i reverse only half cuz palindrome
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return reversed_half == x or x == reversed_half // 10
if __name__ == '__main__':
    num = 0
    s = Solution()
    print(s.isPalindrome(num))
