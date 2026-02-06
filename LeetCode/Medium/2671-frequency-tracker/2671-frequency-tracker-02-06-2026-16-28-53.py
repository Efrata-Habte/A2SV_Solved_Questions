class FrequencyTracker:

    def __init__(self):
        self.container=defaultdict(int)
        self.count=defaultdict(int)

    def add(self, number: int) -> None:
        old=self.container[number]
        if old > 0:
            self.count[old]-=1

        self.container[number]+=1
        self.count[self.container[number]]+=1

    def deleteOne(self, number: int) -> None:
        old=self.container[number]
        if old > 0:
            self.count[old]-=1

        if self.container[number]==0:
            return

        self.container[number]-=1
        self.count[self.container[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.count[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)