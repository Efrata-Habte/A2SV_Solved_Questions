class Solution:
    def frequencySort(self, s: str) -> str:
        char_count=Counter(s)
        char_count=sorted(char_count.items(),key=lambda x:x[1],reverse=True)
        answer=''

        for char,count in char_count:
            answer+= char*count
        return answer