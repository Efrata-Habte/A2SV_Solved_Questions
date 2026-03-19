import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
        
    n = int(input[0])
    k = int(input[1])
    a = list(map(int, input[2:]))

    freq = [0] * 100001
    
    unique_count = 0
    l = 0
    total_good_segments = 0

    for r in range(n):
        if freq[a[r]] == 0:
            unique_count += 1
        freq[a[r]] += 1
        
        while unique_count > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                unique_count -= 1
            l += 1
        
        total_good_segments += (r - l + 1)

    print(total_good_segments)

if __name__ == "__main__":
    solve()