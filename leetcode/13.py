#!usr/bin/python
# -*- coding:UTF-8 -*-

# 13.leetcode题目讲解（Python）：罗马数字转整数

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_id = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        c = 0
        num = 0

        for i in range(len(s) - 1, -1, -1):

            j = roman_id[s[i]]
            print(j)
            # 如果当前字符小于上次迭代的字符，那么属于特殊请求（e.g.,CD,IV..）
            if j < c:
                num -= j
            # 否则直接相加
            if j >= c:
                num += j
            c = j
        return num

a=Solution()
s="MCMXCIV"
print(a.romanToInt(s))