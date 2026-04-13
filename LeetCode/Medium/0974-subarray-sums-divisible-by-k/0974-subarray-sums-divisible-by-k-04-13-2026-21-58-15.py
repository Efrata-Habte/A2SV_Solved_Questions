class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = {0:1}
        running_sum = 0

        for n in nums:
            running_sum += n
            remainder = running_sum % k

            if remainder in prefix:
                count += prefix[remainder]
                prefix[remainder] += 1
            else:
                prefix[remainder] = 1

        return count           