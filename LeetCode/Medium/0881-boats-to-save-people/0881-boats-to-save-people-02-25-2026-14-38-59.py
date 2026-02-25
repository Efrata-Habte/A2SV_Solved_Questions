class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        left = 0
        right = len(people) - 1
        count = 0

        while left <= right: 
            if people[right] + people[left] <= limit:
                left += 1
            count += 1
            right -= 1

        return count
