# Brute force approach

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if n == 0:
            return ""

        if n == 1:
            return strs[0]

        common = ""
        i = 0

        while i < len(strs[0]) and i < len(strs[1]):
            if strs[0][i] == strs[1][i]:
                common += strs[0][i]
                i += 1
            else:
                break

        for j, k in enumerate(strs):
            if j < 2:
                continue

            temp = ""
            for c1, c2 in zip(k, common):
                if c1 == c2:
                    temp += c1
                else:
                    break
            common = temp

        return common
