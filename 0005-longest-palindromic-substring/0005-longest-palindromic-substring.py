class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0  # inclusive bounds of best palindrome

        def expand(l: int, r: int) -> None:
            nonlocal start, end
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # palindrome is s[l+1 : r]
            l += 1
            r -= 1
            if r - l > end - start:
                start, end = l, r

        for i in range(len(s)):
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length

        return s[start:end + 1]