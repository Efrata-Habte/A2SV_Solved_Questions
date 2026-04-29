class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate  = defaultdict(int)

        for l in licensePlate:
            l = l.lower()
            if l.isdigit() or l == " ":
                continue
            plate[l]+=1

        found = True
        words = sorted(words, key = lambda x : len(x))

        for word in words:
            w = Counter(word)
            found = True
            for i,v in plate.items():
                if i not in w or v > w[i]:
                    found = False
                    break
            
            if found:
                return word
            