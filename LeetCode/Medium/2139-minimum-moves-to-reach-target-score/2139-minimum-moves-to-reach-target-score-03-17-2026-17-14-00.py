class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        double = []
        temp = target

        for i in range(maxDoubles):
            temp //= 2
            if temp >=1:
                double.append(temp)

        double.sort()
        count = 0
        val = 1

        # print(double)

        for i in double:
            count+= (i - val)+1
            val = 2*i

        return count + (target - val)
        
        return count
        

