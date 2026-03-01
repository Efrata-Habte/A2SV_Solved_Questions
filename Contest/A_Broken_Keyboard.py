t = int(input())
for _ in range(t):
    word = input()
    res = ""
    
    i = 0
    while i < len(word):
        
        if i + 1 < len(word) and word[i] == word[i+1]:
            i += 2  
        else:
            res += word[i]
            i += 1
    
  
    res = "".join(sorted(set(res)))
    print(res)