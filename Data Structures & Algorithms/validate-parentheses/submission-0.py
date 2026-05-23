class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        valid_open = "([{"

        for c in s:
            if c in valid_open:
                stack.append(c)
            elif dic[c] == stack[-1]:
                stack.pop()
        if len(stack) == 0:
            return True
        return False           