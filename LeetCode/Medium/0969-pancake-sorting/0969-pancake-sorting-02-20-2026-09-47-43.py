class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        i=len(arr)
        steps=[]
        while sorted(arr)!=arr:
            max_idx = arr.index(max(arr[:i]))+1
            if max_idx != i:
                arr[:max_idx]=arr[:max_idx][::-1]
                steps.append(max_idx)
                arr[:i]=arr[:i][::-1]
                steps.append(i)
            i-=1
            print(arr)
        
        return steps