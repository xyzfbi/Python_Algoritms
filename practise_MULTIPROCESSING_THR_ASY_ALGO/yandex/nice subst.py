"""A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

"""
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n < 2:
            return ""
        uniqchars = set(s)
        for i, char in enumerate(s):
            if char.swapcase() not in uniqchars:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])

                return s1 if len(s1) > len(s2) else s2
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.longestNiceSubstring("abABaba"))