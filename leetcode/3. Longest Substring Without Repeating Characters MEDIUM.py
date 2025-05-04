"""
3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint

Given a string s, find the length of the longest

without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = defaultdict(int)
        max_len = 0
        left = 0
        for right in range(len(s)):
            if s[right] in chars and chars[s[right]] >= left:
                left = chars[s[right]] + 1
            chars[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
