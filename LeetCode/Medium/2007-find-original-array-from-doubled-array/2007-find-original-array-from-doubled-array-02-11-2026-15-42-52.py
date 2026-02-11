class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        changed.sort()
        res = []

        for num in changed:
            if count[num] == 0:
                continue

            count[num] -= 1
            double = num * 2

            if count.get(double, 0) > 0:
                count[double] -= 1
                res.append(num)
            else:
                return []

        return res
