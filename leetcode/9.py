#!usr/bin/python
# -*- coding:UTF-8 -*-

# 09.leetcode题目讲解（Python）：回文数

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        int_r = x
        str_r = str(int_r)
        if str_r == str_r[::-1]:
            print(str_r[::-1])
            return True
        else:
            return False



s=Solution()
x="123212321"
print(s.isPalindrome(x))