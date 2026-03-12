class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        second_map = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        answer = 0
        i = len(s) - 1

        while i >= 0:
            j = i - 1
            if i > 0 and s[j : j + 2] in second_map:
                answer += second_map[s[j : j + 2]]
                print(s[j : j + 2])
                i -= 2
            else:
                answer += mapp[s[i]]
                i -= 1

        return answer
