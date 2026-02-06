class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False
        
        char_map={}
        
        for cs,ct in zip(s,t):
            if cs not in char_map:
                char_map[cs]=ct
            else:
                if char_map[cs]!= ct:
                    return False
        values= list(char_map.values())

        return len(set(values))==len(values)


        # s_count=Counter(s)
        # t_count=Counter(t)

        # for i,j in zip(s_count,t_count):
        #     if s_count[i]!=t_count[j]:
        #         return False
        
        # return True