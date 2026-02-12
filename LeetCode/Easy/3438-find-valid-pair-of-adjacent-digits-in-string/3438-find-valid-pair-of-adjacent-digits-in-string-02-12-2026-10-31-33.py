class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)

        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]

            if a != b:
                if int(a) == count[a] and int(b) == count[b]:
                    return a + b

        return ""
