#!usr/bin/python3
# -*- coding:UTF-8 -*-



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Init
        a ="11"
        b = "1"
        _sum = ""
        carry = 0
        ai = len(a) - 1
        bi = len(b) - 1
        temp = 0
        
        # a + b
        while ai >= 0 or bi >= 0 or carry:
            # Compute temp value
            temp = carry
            if ai >= 0 and a[ai] == '1': temp += 1
            if bi >= 0 and b[bi] == '1': temp += 1
            
            # Carry
            carry = temp // 2
            
            # Add to "sum"
            temp = temp % 2
            if temp == 1: _sum =  "1" + _sum
            else: _sum = "0" + _sum            
            
            # Step
            ai -= 1
            bi -= 1
        
        # Answer
        return _sum

s = Solution()
a ="11"
b = "1"
print(s.addBinary(a,b))