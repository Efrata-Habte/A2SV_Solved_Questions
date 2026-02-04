class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans=[]
        state=False
        buffer=""

        for line in source:
            i=0
            while i<len(line):
                if not state:
                    if i+1<len(line) and line[i:i+2]=='//':
                        break
                    elif i+1<len(line) and line[i:i+2]=='/*':
                        state=True
                        i+=1
                    else:
                        buffer+=line[i]
                else:
                    if state and i+1<len(line) and line[i:i+2]=="*/":
                        state=False
                        i+=1
                i+=1
            
            if not state and buffer:
                ans.append(buffer)
                buffer=""

        return ans
