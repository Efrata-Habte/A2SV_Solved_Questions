class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # find dominant element
        count = Counter(nums)
        dominant = count.most_common()
        dom_element = dominant[0][0]
        dom_count = dominant[0][1]
        n = len(nums)
        left_count = 0
        right_count = dom_count

        for i in range(n-1):
            if nums[i] == dom_element:
                left_count+=1
                right_count-=1
                if left_count*2 > (i+1) and  right_count*2> (n-i-1):
                    return i

        return -1

