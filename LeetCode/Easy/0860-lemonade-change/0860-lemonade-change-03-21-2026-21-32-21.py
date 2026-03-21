class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = []
        ten = []

        for i in bills:
            if i == 5:
                five.append(i)
            elif i == 10 and five:
                ten.append(i)
                five.pop()
            elif i == 20:
                if ten and five:
                    ten.pop()
                    five.pop()
                    continue
                for j in range(3):
                    if five:
                        five.pop()
                    else: 
                        return False
                
            else:
                return False
        return True
            
        