#!usr/bin/python
# -*- coding:UTF-8 -*-

# 14.leetcode题目讲解（Python）：最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #判断是否为空
        if not strs:
            return ""

        # 找到最短的字符串
        shorest = min(strs, key=len)

        # 转换为枚举对象
        for i_th, letter in enumerate(shorest):

            for other in strs:

                if other[i_th] != letter:

                    return shorest[:i_th]

        return shorest

s = Solution()
strs= ["capp","capple","cappl"]
print(s.longestCommonPrefix(strs))
