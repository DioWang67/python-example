#!usr/bin/python3
# -*- coding:UTF-8 -*-


# 20.leetcode题目讲解（Python）：有效的括号

class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s with odd length is not valid
        l = len(s)
        if l % 2 != 0:
            return False

        p = {"(": 1.1, ")": -1.1, "{": 2.22, "}": -2.22, "[": 3.333, "]": -3.333}
        num = [0]

        for c in s:
            if num[-1] + p[c] == 0:
                num.pop()
            else:
                num.append(p[c])
    
        if len(num) != 1:
            return False
        else:
            return True

a=Solution()
s=input("輸入括號")

print(a.isValid(s))