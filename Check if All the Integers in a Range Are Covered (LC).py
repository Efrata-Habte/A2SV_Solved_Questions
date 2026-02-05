class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        combo=set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                combo.add(j)

        target=set()
        for k in range(left,right+1):
            target.add(k)
        return target<=combo
