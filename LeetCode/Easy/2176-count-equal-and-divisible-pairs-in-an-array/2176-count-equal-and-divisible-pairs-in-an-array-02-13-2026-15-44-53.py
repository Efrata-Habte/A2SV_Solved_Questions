class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mapp=defaultdict(list)
        count=0

        for idx,val in enumerate(nums):
            mapp[val].append(idx)

        for key,val in mapp.items():
            if len(val)==1:
                continue
            for i in range(len(val)):
                for j in range(i+1,len(val)):
                    if val[i]*val[j] %k==0:
                        count+=1

        return count
