class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_c = Counter(ransomNote)
        magazine_c =Counter(magazine)

        for char,val in ransomNote_c.items():
            if char not in magazine_c or val>magazine_c[char]:
                return False
        
        return True
            