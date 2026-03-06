class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        return sign * result