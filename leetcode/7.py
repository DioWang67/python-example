#!usr/bin/python
# -*- coding:UTF-8 -*-



# leetcode题目讲解（Python）：反转整数

# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """

#         sx = str(x)
#         if len(sx) == 1:
#             return x
#         sx = sx[::-1]
#         if sx[0] == '0':
#             sx = sx[1:]
#         if sx[-1] == '-':
#             sx = sx[:-1]
#             sx = '-' + sx

#         rev_int = int(sx)
#         if rev_int <= 2 ** 31 - 1 and rev_int >= -(2 ** 31):
#             return rev_int
#         else:
#             return 0


# # test：
# s = Solution()
# # print(s.reverse(453861))


# rev_int = 2 ** 31 - 1
# print(rev_int)



def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    result = 0
    sign = 1 if x >= 0 else -1

    x = abs(x)

    
    while x != 0:
        pop = x % 10
        x //= 10

        # 处理溢出
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
            return 0
        if result < INT_MIN // 10 or (result == INT_MIN // 10 and pop < -8):
            return 0
        
        result = result * 10 + pop
        print(result)
    return sign * result

# 测试例子
print(reverse(123))  # 输出: 321
# print(reverse(-123)) # 输出: -321
# print(reverse(120))  # 输出: 21
