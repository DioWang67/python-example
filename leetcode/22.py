#!usr/bin/python3
# -*- coding:UTF-8 -*-

# 22.leetcode题目讲解（Python）：括号生成



class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                print("b")
                return
            if left < n:
                print("c",left,right)
                backtrack(S+'(', left+1, right)               
            if right < left:
                print("d",left,right)
                backtrack(S+')', left, right+1)
        print("a")
        backtrack()
        return ans

s=Solution()
n=3
print(s.generateParenthesis(n))

# def factorial(n):
#     if n == 0:
#         return 1
#     print(n * factorial(n - 1))
#     return n * factorial(n - 1)
# n = 5
# result = factorial(n)
# print(f"The factorial of {n} is {result}")

#5*4*3*2*1