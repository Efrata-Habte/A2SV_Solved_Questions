class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1=set(list1)
        set2=set(list2)
        common=set1 & set2
        min_index=float(inf)
        ans=[]

        for c in common:
            index_sum=list1.index(c)+list2.index(c)
            if index_sum<=min_index:
              if index_sum<min_index:
                ans.clear()
              ans.append(c)
              min_index=index_sum

        return ans
            
