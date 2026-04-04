class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for char in s:
            if char == '#' and not stack1:
                continue
            elif char == '#':
                stack1.pop()
            else:
                stack1.append(char)

        for char in t:
            if char == '#' and not stack2:
                continue
            elif char == '#':
                stack2.pop()
            else:
                stack2.append(char)
                
        return stack1==stack2