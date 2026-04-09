class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0]*n

        def merge(left,right):
            l, r = 0 , 0
            ans = []

            while l < len(left) and r < len(right):
                if nums[left[l]] > nums[right[r]]:
                    output[left[l]] += len(right) - r
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            ans.extend(left[l:])
            ans.extend(right[r:])
            return ans

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            return merge(merge_sort(left), merge_sort(right))
        
        merge_sort([i for i in range(len(nums))])
        return output