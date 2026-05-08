class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle not in haystack:
            return -1
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0] and haystack[i : i + len(needle)] == needle:
                return i
            i += 1
