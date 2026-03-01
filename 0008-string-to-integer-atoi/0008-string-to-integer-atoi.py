class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            if result > (2**31 - 1 - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1
            
            result = result * 10 + digit
            index += 1
        
        return sign * result