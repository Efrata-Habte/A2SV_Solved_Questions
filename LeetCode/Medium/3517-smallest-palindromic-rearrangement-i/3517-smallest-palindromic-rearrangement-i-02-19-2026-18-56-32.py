class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        s_count = Counter(s)
        s_count = dict(sorted(s_count.items(), key=lambda x: x[0]))
        answer = [""] * len(s)
        start, end = 0, len(s) - 1

        for key, val in s_count.items():
            pairs = val // 2
            for _ in range(pairs):
                answer[start] = key
                answer[end] = key
                start += 1
                end -= 1

        mid_char = ""
        for char in s_count:
            if s_count[char] % 2 == 1:
                mid_char = char
                break

        if mid_char and start == end:
            answer[start] = mid_char

        return "".join(answer)