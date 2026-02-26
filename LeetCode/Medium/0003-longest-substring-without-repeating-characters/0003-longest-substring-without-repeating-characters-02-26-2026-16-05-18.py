class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len =0
        container = set()
        l=0

        for r in range(len(s)):
            while s[r] in container:
                container.remove(s[l])
                l+=1
            container.add(s[r])
            max_len = max (max_len,r-l+1)

        return max_len