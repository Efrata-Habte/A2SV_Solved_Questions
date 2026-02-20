class Solution:
    def customSortString(self, order: str, s: str) -> str:
        custom={}
        alphabet ="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(order)):
            custom[order[i]]=i
        
        for i in s:
            if i not in custom:
                custom[i]=ord(i)
        
        temp=[]
        for i in s:
            temp.append(custom[i])
        
        temp.sort()
        answer=""

        for i in temp:
            for key,val in custom.items():
                if val==i:
                    answer+=key
        return answer


        