class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp = {}
        s_list = s.split(" ")

        if len(s_list)!= len(pattern):
            return False

        for char, word in zip(pattern, s_list):
            if char not in mapp:
                if word in mapp.values():
                    return False
                mapp[char] = word
            else:
                if mapp[char] != word:
                    return False

        return True
