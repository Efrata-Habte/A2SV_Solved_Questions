class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.streak = 0
        self.size = k

    def consec(self, num: int) -> bool:
        
        if num == self.value:
            self.streak+=1
        else:
            self.streak=0
        
        return self.streak >= self.size


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)