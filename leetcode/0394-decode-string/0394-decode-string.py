class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        char_stack = []

        current_num = 0
        current_str = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num*10 + int(ch)

            elif ch == "[":
                num_stack.append(current_num)
                char_stack.append(current_str)

                current_num = 0
                current_str = ""

            elif ch == "]":
                char = char_stack.pop()
                k = num_stack.pop()

                current_str = char + current_str*k
            
            else:
                current_str += ch
            
        return current_str 