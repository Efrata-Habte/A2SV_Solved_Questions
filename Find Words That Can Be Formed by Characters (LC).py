class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length=0
        chars_count=Counter(chars)

        for word in words:
            word_count=Counter(word)
            is_good=True

            for char,count in word_count.items():
                if chars_count[char]<count:
                    is_good=False
                    break

            if is_good:
                length+=len(word)
        return length
