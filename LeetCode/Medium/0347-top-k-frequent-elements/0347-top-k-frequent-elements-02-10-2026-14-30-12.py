class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums=Counter(nums)
        most_common = count_nums.most_common(k)
        return [i[0] for i in most_common]