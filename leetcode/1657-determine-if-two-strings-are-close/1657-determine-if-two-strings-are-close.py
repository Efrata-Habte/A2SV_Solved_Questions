class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        val1 = list(c1.values())
        val2 = list(c2.values())

        key1 = set(c1.keys())
        key2 = set(c2.keys())

        val1.sort()
        val2.sort()

        return val1 == val2 and key1 == key2
