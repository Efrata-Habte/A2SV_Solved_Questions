class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=defaultdict(list)

        for s in strs:
            c=frozenset(Counter(s).items())
            count[c].append(s)

        return list(count.values())