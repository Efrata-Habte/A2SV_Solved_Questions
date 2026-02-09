import random

class RandomizedSet:

    def __init__(self):
        self.container = {}   # value -> index in nums
        self.nums = []        # list of values

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False

        self.container[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.container:
            return False

        idx = self.container[val]
        last = self.nums[-1]

        self.nums[idx] = last
        self.container[last] = idx

        self.nums.pop()
        del self.container[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
