class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for char in string:
                if char == '#' and not stack:
                    continue
                elif char == '#':
                    stack.pop()
                else:
                    stack.append(char)
            return stack
        
        return process(s) == process(t)