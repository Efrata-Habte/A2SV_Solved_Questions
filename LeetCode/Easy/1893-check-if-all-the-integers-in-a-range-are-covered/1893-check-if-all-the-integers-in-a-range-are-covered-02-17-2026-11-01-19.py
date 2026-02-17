class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        container = set()
        
        for r in ranges:
            i = r[0]
            while i <= r[1]:
                container.add(i)
                i += 1

        for i in range(left, right + 1):
            if i not in container:
                return False

        return True
