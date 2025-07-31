class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start, maxLen = 0, 1
        for i in range(n):
            for j in range(2):
                l, h = i, i + j

                while l >= 0 and h <= n and s[l] == s[h]:
                    currLen = h - l + 1
                    if currLen > maxLen:
                        start = l
                        maxLen = currLen

                    l -= 1
                    h += 1

        return s[start: start + maxLen]



def longestPalindrome(s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start, maxLen = 0, 1
        for i in range(n):
            for j in range(2):
                l, h = i, i + j
                while l >= 0 and h < n and s[l] == s[h]:
                    currLen = h - l + 1
                    if currLen > maxLen:
                        start = l
                        maxLen = currLen

                    l -= 1
                    h += 1

        return s[start: start + maxLen]

if __name__ == '__main__':
    print(longestPalindrome("dssfgaskfjdjqfkvbdfgsjxanaxfjidkgfdjgdfgdfjogiidofkgkgodfpdjgdo"))