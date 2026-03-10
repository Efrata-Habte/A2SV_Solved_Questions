class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        answer = []

        for i in nums1:
            idx = nums2.index(i)
            greater = False
            for j in range (idx+1,n):
                if i < nums2[j]:
                    answer.append(nums2[j])
                    greater = True
                    break
            if not greater:
                answer.append(-1)

        return answer
            
            


