class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)

        if needle == haystack:
            return 0

        while r <= len(haystack):
            if haystack[l:r] == needle:
                return l
            else:
                l += 1 
                r += 1
        return -1
