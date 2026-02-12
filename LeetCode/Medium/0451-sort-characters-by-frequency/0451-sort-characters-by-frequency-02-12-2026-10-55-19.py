class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = ""

        count = sorted(count.items(), key=lambda x: -x[1])

        for char, freq in count:
            ans += char * freq

        return ans
