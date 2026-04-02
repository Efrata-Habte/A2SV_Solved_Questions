class DataStream:

    def __init__(self, value: int, k: int):
        self.cont = deque()
        self.val = value
        self.k = k
        self.streak = k

    def consec(self, num: int) -> bool:
        self.cont.append(num)
        if num == self.val:
            self.streak-=1
        
        if len(self.cont) > self.k:
            poped = self.cont.popleft()
            if poped == self.val:
                self.streak +=1

        if len(self.cont) == self.k:
            if self.streak == 0:
                return True
        
        
        return False
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)