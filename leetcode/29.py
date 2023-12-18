class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ############
        #abs()絕對值 
        # XOR 運算符（^） 兩個條件的值不相等時，XOR 運算結果為 True，否則為 False
        # multiple <<= 3   multiple值 *2    <<=3  = *2*2*2 




        #####################
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        if dividend == 0:
            return 0
        
        if divisor == 1:
            return min(max(INT_MIN, dividend), INT_MAX)
        
        if divisor == -1:
            return min(max(INT_MIN, -dividend), INT_MAX)
        
        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor) 
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                print(multiple)
            
            dividend -= temp_divisor
            quotient += multiple
        
        quotient = -quotient if is_negative else quotient
        return min(max(INT_MIN, quotient), INT_MAX)

# 創建 Solution 的實例
s = Solution()

# 設定 dividend 和 divisor 的值
dividend = -50
divisor = -4

# 呼叫 divide 方法並印出結果
# print(s.divide(dividend, divisor))

multiple = 3
multiple <<= 3
print(multiple)
