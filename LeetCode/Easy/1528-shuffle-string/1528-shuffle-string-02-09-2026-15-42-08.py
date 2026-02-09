class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapp={}
        ans=""

        for idx,char in zip(indices,s):
            mapp[idx]=char

        for i in range(len(s)):
            ans+=mapp[i]
        
        return ans